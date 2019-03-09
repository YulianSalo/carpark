class Car(object):
	"""docstring for ClassName"""
	def __init__(self, carID, make, model, year, numberPlate, color, owner, place):
		self.carID = carID
		self.make = make
		self.model = model
		self.year = year
		self.numberPlate = numberPlate
		self.color = color
		self.owner = owner
		self.place = place	

	def getCarID(self):
		return carID

	def getMake(self):
		return self.make	

	def getModel(self):
		return self.model

	def getYear(self):
		return self.year

	def getNumberPlate(self):
		return self.numberPlate
	
	def getColor(self):
		return self.color

	def getOwner(self):
		return self.owner

	def getPlace(self):
		return self.place

	def setCarID(self, carID):
		self.carID = carID

	def setMake(self, make):
		self.make = make	

	def setModel(self, model):
		self.model = model
	
	def setYear(self, year):
		self.year = year

	def setNumberPlate(self, numberPlate):
		self.numberPlate = numberPlate

	def setColor(self, color):
		self.color = color

	def setOwner(self, owner):
		self.owner = owner

	def setPlace(self, place):
		self.place = place

	def __str__(self):
		return 'Car ID: {} Make: {}: Model: {} Year: {} numberPlate: {} Color: {} Owner(s): {} Place: {} \n'.format(
			self.carID,
			self.make,
			self.model, 
			self.year, 
			self.numberPlate, 
			self.color, 
			self.owner, 
			self.place)


	def carInput():
		
		carId = input("carID: ")

		file = "carpark.txt"

		carNewId = carIdCheck(file, carId)

		carId = carNewId

		carMake = input("Make: ")
		
		carModel = input("Model: ")

		carYear = input("Year: ")

		carNumberPlate = input("Number Plate: ")

		carNewNumberPlate = carCheck(file, carNumberPlate)

		carNumberPlate = carNewNumberPlate

		carColor = input("Color: ")

		carOwner = input("Owner: ")

		carPlace = input("Place: ")

		carNewPlace = carCheck(file, carPlace)

		carPlace = carNewPlace

		carInCarPark = Car(
			carID = carId,
			make = carMake, 
			model = carModel, 
			year = carYear, 
			numberPlate = carNumberPlate, 
			color = carColor, 
			owner = carOwner, 
			place = carPlace)		

		return carInCarPark

