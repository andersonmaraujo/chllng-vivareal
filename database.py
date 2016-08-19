import sqlite3
import requests
from entities.property import Property
from entities.province import Province
from flask import Flask, g, json
app = Flask(__name__)

def init_db():
	with app.app_context():
		db = get_db()
		with app.open_resource('schema.sql', mode='r') as f:
		    db.cursor().executescript(f.read())
		db.commit()
		config()

@app.cli.command('initdb')
def initdb_command():
	init_db()
	print "Base criada!!"
	config()

def config():
	with app.app_context():
		r = requests.get("https://raw.githubusercontent.com/VivaReal/code-challenge/master/properties.json")

		for entry in json.loads(r.text)['properties']:
			property = Property(entry['lat'], entry['long'], entry['title'], entry['price'], entry['description'], entry['beds'], entry['baths'], entry['squareMeters'])
			createProperty(property)

		r = requests.get("https://raw.githubusercontent.com/VivaReal/code-challenge/master/provinces.json")

		createProvince(Province('Gode', json.loads(r.text)['Gode']))
		createProvince(Province('Ruja', json.loads(r.text)['Ruja']))
		createProvince(Province('Jaby', json.loads(r.text)['Jaby']))
		createProvince(Province('Scavy', json.loads(r.text)['Scavy']))
		createProvince(Province('Groola', json.loads(r.text)['Groola']))
		createProvince(Province('Nova', json.loads(r.text)['Nova']))
		return "Concluido."

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect('vivareal.db')
	db.row_factory = make_dicts	
	return db

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))

@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()

def getProvincesOfProperty(x, y):
	provinces = query_db('select name from provinces where (upperLeftX <= ? and bottomRightX >= ?) and (bottomRightY <= ? and upperLeftY >= ?)', [x, x, y, y])
	return provinces

def createProperty(property):
	cursor = get_db().cursor()
	cursor.execute("""
	INSERT INTO properties (x, y, title, price, description, beds, baths, squareMeters)
	VALUES (?,?,?,?,?,?,?,?)
	""", (property.x, property.y, property.title, property.price, property.description, property.beds, property.baths, property.squareMeters))
	get_db().commit()

def createProvince(province):
	cursor = get_db().cursor()
	cursor.execute("""
	INSERT INTO provinces (name, upperLeftX, upperLeftY, bottomRightX, bottomRightY)
	VALUES (?,?,?,?,?)
	""", (province.name, province.upperLeftX, province.upperLeftY, province.bottomRightX, province.bottomRightY))
	get_db().commit()

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv
