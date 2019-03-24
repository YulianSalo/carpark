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

	choice  = (input("Your choice:"))

	print("\n")

	if choice == "1":

		'''Input data '''

		infile = "carpark.txt"

		if not os.path.exists(infile):

			carstore = open(infile, "w+")

		else:

			carstore = open(infile, "a")

		carInCarPark = Car.carInput(infile)

		carstore.write(str(carInCarPark))

		carstore.close()

		print("\n")

		main()

	elif choice == "2":

		'''Search specific data '''

		carIdSearch = input('Enter the search parameter: ')

		lines = []

		with open('carpark.txt') as f:

			for row in f:

				lines.append(row)


			for line in lines:

				if carIdSearch in line:
					print(line)

		main()
    	
	elif choice == "3":

		'''See all data '''

		carstore = open("carpark.txt", "r")
		
		carstore_display = carstore.read()
		
		#Car.defaultPrint()
		print(carstore_display)

		print("\n")

		main()		

	elif choice == "4":

		''' Modify data ''' 
		
		carIdSearch = input('Enter the ID : ')

		modlist = []

		sortId = idSearch(infile)

		infile = "carpark.txt"

		outfile = "carparkMod.txt"

		lines = readInList(infile)

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

		infile = "carpark.txt"

		outfile = "carparkMod.txt"


		carIdSearch = input('Enter the ID : ')

		lines = []

		sortId = idSearch(infile)

		lines = readInList(infile)

		for line in lines:

			if carIdSearch in line and carIdSearch in sortId:

				print(line)

				deleteDesicion = input("Do you want to delete the record? Y/N: ")

				if deleteDesicion == 'y' or deleteDesicion == 'Y':

					lines.remove(line)

					reWrite(infile, outfile, lines)
				
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
	
