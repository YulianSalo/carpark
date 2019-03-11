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


def main():

	menu()

	choice  = input("Your choice:")

	print("\n")

	if choice == "1":

		'''Input data '''

		if not os.path.exists("carParkSort.txt"):
			
			carstore = open("carParkSort.txt", "w+")

		else:

			carstore = open("carParkSort.txt", "a")

		carInCarPark = Car.carInput()

		carstore.write(str(carInCarPark))

		carstore.close()

		infile = "carParkSort.txt"

		outfile = "carparkMod.txt"

		lines = readInList(infile)

		lines.sort()

		reWrite(infile, outfile, lines)

		print("\n")

		main()

	elif choice == "2":

		'''Search specific data '''

		carIdSearch = input('Enter the search parameter: ')
		#carParam = input('Enter the parameter: ')

		lines = []

		with open('carParkSort.txt') as f:

			for row in f:

				lines.append(row)


			for line in lines:

				if carIdSearch in line:
					print(line)

		main()
    	
	elif choice == "3":

		'''See all data '''

		infile = "carParkSort.txt"

		outfile = "carparkMod.txt"

		lines = readInList(infile)

		lines.sort()

		with open(outfile, "w") as f1:

			with open(infile, "r+") as f:

				for line in lines:

					f1.write(line)

			f1.close()
		
		f.close()

		os.rename(outfile, infile)

		carstore = open("carParkSort.txt", "r")
		
		carstore_display = carstore.read()

		print(carstore_display)

		print("\n")

		main()		

	elif choice == "4":

		''' Modify data ''' 
		
		carIdSearch = input('Enter the ID : ')
		
		modlist = []

		infile = "carParkSort.txt"

		outfile = "carparkMod.txt"

		sortId = idSearch(infile)

		lines = readInList(infile)

		lines.sort()

		with open(outfile, "w") as f1:

			with open(infile, "r+") as f:

				for line in lines:

					if carIdSearch in line and carIdSearch in sortId:

						print(line)

						modlist.append(input("Field to modify: "))
						
						newfield = input("New data: ")

					for word in modlist:
							
							line = line.replace(word, newfield )
					
					f1.write(line)

				f1.close()
			
			f.close()

		os.rename(outfile, infile)

		main()

	elif choice == "5":

		''' Delete data '''

		infile = "carParkSort.txt"

		outfile = "carparkMod.txt"

		carIdSearch = input('Enter the ID : ')

		sortId = idSearch(infile)

		lines = readInList(infile)

		lines.sort()

		for line in range (len(lines)):

			if carIdSearch in lines[line] and carIdSearch in sortId[line]:

				print(lines[line])

				deleteDesicion = input("Do you want to delete the record? Y/N: ")

				if deleteDesicion == 'y' or deleteDesicion == 'Y':

					lines.remove(lines[line])

					sortId.remove(sortId[line])

					reWrite(infile, outfile, lines)

					reWrite("idList.txt", "idListMod.txt", sortId)
				
					print("\nDone.\n ")

					main()
				
				elif deleteDesicion == 'n' or deleteDesicion == 'N':
				
					main()

				else:
					
					print("Wrong button pressed. Returning to main menu.")

					main()

	elif choice == "6":

		''' Exit ''' 
		
		print("Bye!")

		exit()

	else:
		
		print("Wrong button pressed.")
		
		main()

if __name__ == '__main__':
	main()
	
