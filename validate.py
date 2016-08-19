from voluptuous import Invalid

def ValidateAreaX(value):
	if int(value) >= 0 and int(value) <= 1400:
		return value
	raise Invalid("Not a valid area") 

def ValidateAreaY(value):
	if int(value) >= 0 and int(value) <= 1000:
		return value
	raise Invalid("Not a valid area")

def ValidateSimpleStrings(value):
	if isinstance(value, str) and len(value) > 0:
		return value
	raise Invalid("Not a valid string")

def ValidatePrice(value):
	if float(value) > 0:
		return value
	raise Invalid("Not a valid price")

def ValidateBeds(value):
	if int(value) >= 1 and int(value) <= 5:
		return value
	raise Invalid("Not a valid value")

def ValidateBaths(value):
	if int(value) >= 1 and int(value) <= 4:
		return value
	raise Invalid("Not a valid baths")

def ValidateSquareMeters(value):
	if float(value) >= 20 and float(value) <= 240:
		return value
	raise Invalid("Not a valid square meters")