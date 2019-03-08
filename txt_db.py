import os

def menu():
	print("""Please choose an action to start:
		1. Input data.
		2. Search specific data.
		3. See all data.
		4. Modify data.
		5. Delete data.  
		6. Exit\n""")

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


def carIdCheck(file, param):

	lines = []

	with open(file) as f:

		for row in f:

			lines.append(row)

		for line in lines:

			if param in line:

				print("Current data is in use. Try another one.")

				param = input("Car new data: ")
				
				carCheck(file, param)

	return param

def carCheck(file, param):

	lines = []

	with open(file) as f:

		for row in f:

			lines.append(row)

		for line in lines:

			if param in line:

				print("Current data is in use. Try another one.")

				param = input("Car new data: ")
				
				carCheck(file, param)

	return param

def main():

	menu()

	choice  = (input("Your choice:"))

	print("\n")

	if choice == "1":
		if not os.path.exists("carpark.txt"):
			carstore = open("carpark.txt", "w+")

		else:

			carstore = open("carpark.txt", "a")


		carInCarPark = Car.carInput()

		carstore.write(str(carInCarPark))

		carstore.close()

		print("\n")

		main()

	elif choice == "2":

		carIdSearch = input('Enter the search parameter: ')
		#carParam = input('Enter the parameter: ')

		lines = []

		with open('carpark.txt') as f:

			for row in f:

				lines.append(row)


			for line in lines:

				if carIdSearch in line:
					print(line)

		main()
    	
	elif choice == "3":

		carstore = open("carpark.txt", "r")
		
		carstore_display = carstore.read()
		
		print(carstore_display)

		print("\n")

		main()		

	elif choice == "4":

		#carstore = open("carstore.txt", "w+")
		
		carIdSearch = input('Enter the ID : ')
		#carParam = input('Enter the parameter: ')

		lines = []
		modlist = []

		infile = "carpark.txt"
		outfile = "carparkMod.txt"

		with open('carpark.txt') as f:

			for row in f:

				lines.append(row)

			fin = open(infile, "r+")
			fout = open(outfile, "w+")

			for line in lines:

				if carIdSearch in line:
					print(line)
					modlist.append(input("Field to modify:"))
					newfield = input("New data:")

					for word in modlist:
						line = line.replace(word, newfield )
				fout.write(line)
			fin.close()
		#infile.seek(0)
		#infile.truncate()
		with open(outfile) as f:
			with open(infile, "w") as f1:
				for line in f:
					f1.write(line)

		fout.close()




		main()

	elif choice == "5":

		carIdSearch = input('Enter the ID : ')
		#carParam = input('Enter the parameter: ')

		lines = []
		modlist  = []

		with open('carpark.txt') as f:

			for row in f:

				lines.append(row)


			for i  in range(len(lines)):

				if carIdSearch in lines[i]:
					print(lines[i], "\n")
					lines.remove(lines[i])
			for line in lines:
				f.write()


	elif choice == "6":
		
		print("Bye!")

		exit()

	else:
		
		print("Wrong button pressed.")
		
		main()

if __name__ == '__main__':
	main()
	
