class Province(object):
	name = None
	upperLeftX = None
	upperLeftY = None
	bottomRightX = None
	bottomRightY = None

	def __init__(self, name, upperLeftX, upperLeftY, bottomRightX, bottomRightY):
		self.name = name
		self.upperLeftX = x
		self.upperLeftY = y
		self.bottomRightX = bottomRightX
		self.bottomRightY = bottomRightY

	def __init__(self, name, json):
		self.name = name
		self.upperLeftX = json['boundaries']['upperLeft']['x']
		self.upperLeftY = json['boundaries']['upperLeft']['y']
		self.bottomRightX = json['boundaries']['bottomRight']['x']
		self.bottomRightY = json['boundaries']['bottomRight']['y']