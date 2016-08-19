from province import Province

class Property(object):
	id = None
	x = None
	y = None
	title = None
	price = None
	description = None
	beds = None
	baths = None
	squareMeters = None
	provinces = []

	def __init__(self, x, y, title, price, description, beds, baths, squareMeters):
		self.x = x
		self.y = y
		self.title = title
		self.price = price
		self.description = description
		self.beds = beds
		self.baths = baths
		self.squareMeters = squareMeters

	def setProvinces(self, provinces):
		self.provinces = provinces

	def setWithJSON(self, json):
		self.id = json['id']
		self.x = int(json['lat'])
		self.y = json['long']
		self.title = json['title']
		self.price = json['price']
		self.description = json['description']
		self.beds = json['beds']
		self.baths = json['baths']
		self.squareMeters = json['squareMeters']