import os
from index_objects import (
	Car as Car)
from methods import (
	carCheck as carCheck,
	menu as menu,
	idSearch as idSearch,
	readInList as readInList,
	reWrite as reWrite,
	createFile as createFile,
	readInIndexList as readInIndexList)
import re

def main():

	infile = "indexCar.txt"

	outfile = "carparkMod.txt"

	indexInFile  = "indexBlocks.txt"

	menu()

	choice  = (input("Your choice:"))

	print("\n")

	if choice == "1":

		'''Input data '''

		carstore = createFile(infile)

		indexFile = createFile(indexInFile)

		carInCarPark = Car.carInput(infile)

		carstore.write(str(carInCarPark))

		carstore.close()

		lines = readInList(infile)

		lines.sort()

		reWrite(infile, outfile, lines)

		getCarId = str(carInCarPark.getCarID())

		getBlock = str(carInCarPark.getBlock())

		indexBlock = getCarId + " " + getBlock

		indexFile.write(indexBlock)

		indexFile.close()

		indexLines = readInList(indexInFile)

		indexLines.sort()

		reWrite(indexInFile,outfile, indexLines) 

		print("\n")

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

		indexFile = createFile(indexInfile)

		#carstore = createFile(infile)

		indexLines = readInIndexList(infile)

		indexLines.sort()

		reWrite(indexInfile, outfile, indexLines)

		main()

	else:
		
		print("Wrong button pressed.")
		
		main()



if __name__ == '__main__':
	main()
	
