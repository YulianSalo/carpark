import re

def menu():
	print("""Please choose an action to start:
		1. Input data.
		2. Search specific data.
		3. See all data.
		4. Modify data.
		5. Delete data.  
		6. Exit.
		7. Delete file.\n""")

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
def idRegEx(carId):

	if len(carId) == 4:
		for i in range(len(carId)):

			if re.match(r"\d\d\d\d", carId):
				return carId
			else:
				newCarId = input("Your input is incorrect. Please, reenter it in such a way: 0000. Your input: ")
				idRegEx(newCarId)

	else:
		newCarId = input("Your input is incorrect. Please, reenter it in such a way: 0000. Your input: ")
		idRegEx(newCarId)


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
