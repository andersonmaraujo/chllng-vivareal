import database as db
import requests
from validate import *
from entities.property import Property
from entities.province import Province
from voluptuous import Schema, Required, Invalid, MultipleInvalid
from flask import Flask, render_template, request, json, jsonify, Response
app = Flask(__name__)

@app.route("/properties", methods=['GET', 'POST'])
def properties():
	if request.method == 'POST':
		s = Schema({
			Required("x"): ValidateAreaX,
			Required("y"): ValidateAreaY,
			Required("title"): ValidateSimpleStrings,
			Required("description"): ValidateSimpleStrings,
			Required("price"): ValidatePrice,
			Required("beds"): ValidateBeds,
			Required("baths"): ValidateBaths,
			Required("squareMeters"): ValidateSquareMeters
			})
		
		property = Property(request.form["x"], request.form["y"], request.form["title"], request.form["price"], request.form["description"], request.form["beds"], request.form["baths"], request.form["squareMeters"])

		try:
			s({
				"x": property.x,
				"y": property.y,
				"title": str(property.title),
				"description": str(property.description),
				"price": property.price,
				"beds": property.beds,
				"baths": property.baths,
				"squareMeters": property.squareMeters
				})
		except MultipleInvalid as e:
			RESULTS = {
				'error': {
					'status': 400,
					'message': str(e)
				}
			}
			return Response(json.dumps(RESULTS), status=400, mimetype='application/json')

		db.createProperty(property)
		property.provinces = db.getProvincesOfProperty(property.x, property.y)

		RESULTS = {
			'provinces': property.provinces
		}

		return Response(json.dumps(RESULTS), status=200, mimetype='application/json')
	else:
		s = Schema({
				Required("ax"): ValidateAreaX,
				Required("ay"): ValidateAreaY,
				Required("bx"): ValidateAreaX,
				Required("by"): ValidateAreaY
			})

		try:
			s({
				"ax": request.args.get("ax", -1),
				"ay": request.args.get("ay", -1),
				"bx": request.args.get("bx", -1),
				"by": request.args.get("by", -1)
			})
		except MultipleInvalid as e:
			RESULTS = {
				'error': {
					'status': 400,
					'message': str(e)
				}
			}
			return Response(json.dumps(RESULTS), status=400, mimetype='application/json')

		properties_results = db.query_db(
			"""select * from properties where x >= ? and x <= ? and y >= ? and y <= ?"""
			, (int(request.args.get("ax")), int(request.args.get("bx")), int(request.args.get("ay")), int(request.args.get("by")))
			)

		RESULTS = {
			'foundProperties': len(properties_results),
			'properties': []
			}
		for entry in properties_results:
			entry['provinces'] = db.getProvincesOfProperty(entry['x'], entry['y'])
			RESULTS['properties'].append(entry)

		return Response(json.dumps(RESULTS), status=200, mimetype='application/json')

@app.route("/properties/<int:propertieid>")
def properties_detail(propertieid):
	property = db.query_db('select * from properties where id = ?', [propertieid], one=True)
	if property is None:
		RESULTS = {
			'error': {
				'status': 400,
				'message': 'No property found.'
			}
		}
		return Response(json.dumps(RESULTS), status=400, mimetype='application/json')
	else:
		property['provinces'] = db.getProvincesOfProperty(property['x'], property['y'])
		return Response(json.dumps(property), status=200, mimetype='application/json')

@app.route("/reset_properties")
def reset_properties():
	cursor = db.get_db().cursor()
	cursor.execute("""
		DELETE FROM properties
		""")
	db.get_db().commit()
	return "Deleted!"

if __name__ == "__main__":
	app.run()