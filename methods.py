import re
import os

def menu():
	print("""Please choose an action to start:
		1. Input data.
		2. Search specific data.
		3. See all data.
		4. Modify data.
		5. Delete data.  
		6. Exit.\n""")

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


def idSearch(workingFile):
	
	lines = []

	sortId = []

	gotId = " "

	#workingFile = "carParkSort.txt"

	with open(workingFile, "r+") as f:
		
		for row in f:
			#for i in range(4):
			lines.append(row)
		
		for line in lines:
			
			for i in range(len(line)):
				
				gotId = line[0] + line[1] + line[2] + line[3]

			sortId.append(str(gotId))

		with open("idList.txt", "w") as f1:

			with open(workingFile, "r+") as f:
			
				for sId in sortId:

					f1.write(sId)

				f1.close()

			f.close()

	return sortId


def readInList(infile):

	lines = []

	with open(infile, "r+") as f:

		for row in f:

			lines.append(row)

		f.close()

	return lines


def reWrite(file1, file2, lines):

	with open(file2, "w") as f1:

		with open(file1, "r+") as f:
		
			for line in lines:

				f1.write(line)

			f1.close()

		f.close()

	os.rename(file2, file1)


def createFile(infile):

	''' creates file  '''

	if not os.path.exists(infile):

		carstore = open(infile, "w+")

	else:

		carstore = open(infile, "a")

	return carstore

def readInIndexList(infile):

	lines = []

	indexLines = []

	with open(infile, "r+") as f:

		for row in f:
			#for i in range(4):
			lines.append(row)
		
		for i in range(len(lines)):
				
			gotId = lines[i][0] + lines[i][1] + lines[i][2] + lines[i][3]

			print(lines[i][-2])

			blockId = lines[i][-2]

			indexRow = gotId + " " + blockId + "\n"

			indexLines.append(indexRow)

		f.close()

		#print(lines)

	return indexLines
