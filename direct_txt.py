import os
from objects import (
	Car as Car)
from methods import (
	carCheck as carCheck,
	menu as menu,
	idSearch as idSearch,
	readInList as readInList,
	reWrite as reWrite)
import re

import gc 



def main():

	blockZero = []

	blockOne = []

	blockTwo = []

	blockThree = []

	blockFour = []

	blockFive = []

	blockSix = []

	blockSeven = []

	blockEight = []

	blockNine = []

	listZero = []

	listOne = []

	listTwo = []

	listThree = []

	listFour = []

	listFive = []

	listSix = []

	listSeven = []

	listEight = []

	listNine = []

	overflowBuffZero = []

	overflowBuffOne = []

	overflowBuffTwo = []

	overflowBuffThree = []

	overflowBuffFour = []

	overflowBuffFive = []

	overflowBuffSix = []

	overflowBuffSeven = []

	overflowBuffEight = []

	overflowBuffNine = []

	blockLen  = 5

	#blockExample = [listExample, OverflowBuffExample]

	listBlocks = [
		blockZero, 
		blockOne, 
		blockTwo, 
		blockThree, 
		blockFour, 
		blockFive, 
		blockSix, 
		blockSeven, 
		blockEight, 
		blockNine
		]

	listLists = [
		listZero, 
		listOne, 
		listTwo, 
		listThree, 
		listFour, 
		listFive, 
		listSix, 
		listSeven, 
		listEight, 
		listNine
		]

	listOverflowBuff = [
		overflowBuffZero, 
		overflowBuffOne, 
		overflowBuffTwo, 
		overflowBuffThree, 
		overflowBuffFour,
	 	overflowBuffFive, 
	 	overflowBuffSix, 
	 	overflowBuffSeven, 
	 	overflowBuffEight, 
	 	overflowBuffNine
	 	]

	for i in range(len(listBlocks)):

		listBlocks[i].append(listLists[i])

		listBlocks[i].append(listOverflowBuff[i])

		for j in range(blockLen): 

			listLists[i].append(None)


	#print(listBlocks)

	infile = "directCar.txt"

	outfile = "carparkMod.txt"

	counter = 0

	with open(infile, "r+")as f:

		for row in f:

			counter +=1

	with open(infile, "r+") as f:

		for row in f:

			for i in range(len(listBlocks)):

					for j in range(counter):

						if j < 5:

							if row[3] == str(i) and listLists[i][j] is None:


								listLists[i][j] = row

								break

						if row[3]== str(i) and listLists[i][4] is not None and j >= 5 :

							listOverflowBuff[i].append(row)

							break

	f.close()


	menu()

	choice  = (input("Your choice:"))

	print("\n")

	if choice == "1":

		'''Input data '''

		if not os.path.exists(infile):

			carstore = open(infile, "w+")

		else:

			carstore = open(infile, "a")

		carInCarPark = Car.carInput()

		getCarId = str(carInCarPark.getCarID())

		for i in range(len(listBlocks)):

			for j in range(len(listLists[i])):

				if getCarId[-1] == str(i) and listLists[i][j] == None :

					listLists[i][j] = str(carInCarPark)

					carstore.write(str(listLists[i][j]))

					break

				elif getCarId[-1] == str(i) and listLists[i][4] != None:

					listOverflowBuff[i].append(str(carInCarPark))

					carstore.write(str(listOverflowBuff[i][-1]))

					break



		print(listBlocks)

		carstore.close()

		print("\n")

		lines = readInList(infile)

		lines.sort()

		with open(outfile, "w") as f1:

			with open(infile, "r+") as f:

				for line in lines:

					f1.write(line)

			f1.close()
		
		f.close()

		os.rename(outfile, infile)

		main()

	elif choice == "2":

		'''Search specific data '''

		result = 0

		carIdSearch = input('Enter the ID : ')

		blockId = int(carIdSearch[3])

		for i in range (len(listLists[blockId])):

			if carIdSearch in listLists[blockId][i]:

				print(listLists[blockId][i])

				result = 1

				break

		for i in range(len(listOverflowBuff[blockId])):

			if carIdSearch in listOverflowBuff[blockId][i]:

				print(listOverflowBuff[blockId][i])

				result = 1

				break

		if result == 0:

			print("No match found.")

		main()
    	
	elif choice == "3":

		'''Read all data'''


		for i in range(len(listBlocks)):

			print("Block #", i, "\n")
			
			for j in range(blockLen):

				if listLists[i][j] != None:

					print(listLists[i][j])

			if listOverflowBuff != []:

				for j in range(len(listOverflowBuff[i])):
				
					print("Overflow buffer #{}: {}".format(i, listOverflowBuff[i][j]))

			print("=================")

		print("\n")

		lines = readInList(infile)

		lines.sort()

		with open(outfile, "w") as f1:

			with open(infile, "r+") as f:

				for line in lines:

					f1.write(line)

			f1.close()
		
		f.close()

		os.rename(outfile, infile)

		main()		

	elif choice == "4":

		''' Modify data ''' 
		
		carIdSearch = input('Enter the ID : ')

		blockId = int(carIdSearch[3])

		modlist = []

		lines = []

		result = 0

		for i in range (len(listLists[blockId])):

			if carIdSearch in listLists[blockId][i]:

				print(listLists[blockId][i])

				oldField = input("Field to modify: ")
					
				newField = input("New data: ")
					
				listLists[blockId][i] = listLists[blockId][i].replace(oldField, newField )

				result = 1 

				break

		for i in range(len(listOverflowBuff[blockId])):

			if carIdSearch in listOverflowBuff[blockId][i]:

				print(listOverflowBuff[blockId][i])

				oldField = input("Field to modify: ")
					
				newField = input("New data: ")
					
				listOverflowBuff[blockId][i] = listOverflowBuff[blockId][i].replace(oldField, newField )

				result = 1 

				break

		if result == 0:

			print("No match found.")

		elif result == 1:

			with open(infile, "w+") as f1:

				for i in range(len(listBlocks)):

					for j in range(blockLen):

						if listLists[i][j] is not None:
					
							f1.write(str(listLists[i][j]))

					for k in range(len(listOverflowBuff[i])):
				
						f1.write(str(listOverflowBuff[i][k]))

			f1.close()

		with open(outfile, "w") as f1:

			with open(infile, "r+") as f:

				for line in lines:

					f1.write(line)

			f1.close()
		
		f.close()

		os.rename(outfile, infile)


		main()

	elif choice == "5":

		''' Delete data '''

		carIdSearch = input('Enter the ID : ')

		blockId = int(carIdSearch[3])

		modlist = []

		lines = []

		result = 0

		'''Checking if car is in main buffer'''

		for i in range (len(listLists[blockId])):

			if carIdSearch in listLists[blockId][i]:

				print(listLists[blockId][i])

				deleteDesicion = input("Do you want to delete the record? Y/N: ")

				if deleteDesicion == 'y' or deleteDesicion == 'Y':
						
					listLists[blockId][i] = None

					if listOverflowBuff[i] != []:

						listLists[blockId][i] = listOverflowBuff[i][0]

						listOverflowBuff[i].pop(0)

						break

					result = 1 

					break

				elif deleteDesicion == 'n' or deleteDesicion == 'N':
				
					main()

				else:
					
					print("Wrong button pressed. Returning to main menu.")

					main()

		'''Checking if car is in overflow buffer'''

		for i in range(len(listOverflowBuff[blockId])):

			if carIdSearch in listOverflowBuff[blockId][i]:

				print(listOverflowBuff[blockId][i])

				deleteDesicion = input("Do you want to delete the record? Y/N: ")

				if deleteDesicion == 'y' or deleteDesicion == 'Y':
						
					listOverflowBuff[i].pop(i)

					result = 1 

					break

				elif deleteDesicion == 'n' or deleteDesicion == 'N':
				
					main()

				else:
					
					print("Wrong button pressed. Returning to main menu.")

					main()

		if result == 0:

			print("No match found.")

		elif result == 1:

			with open(infile, "w+") as f1:

				for i in range(len(listBlocks)):

					for j in range(blockLen):

						if listLists[i][j] is not None:
					
							f1.write(str(listLists[i][j]))

					for k in range(len(listOverflowBuff[i])):
				
						f1.write(str(listOverflowBuff[i][k]))

			f1.close()

		listBlocks = None

		main()

	elif choice == "6":

		''' Exit ''' 
		
		print("Bye!")

		exit()

	elif choice == "0":

		print("Programming God's mode is not implemented yet.")

		main()

	else:
		
		print("Wrong button pressed.")
		
		main()

if __name__ == '__main__':
	main()
	
