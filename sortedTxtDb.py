import os
from objects import (
	Car as Car)
from methods import menu as menu
from methods import (carCheck as carCheck)
import re


def main():

	menu()

	choice  = input("Your choice:")

	print("\n")

	if choice == "1":

		'''Input data '''

		if not os.path.exists("carpark.txt"):
			
			carstore = open("carpark.txt", "w+")

		else:

			carstore = open("carpark.txt", "a")

		carInCarPark = Car.carInput()

		carstore.write(str(carInCarPark))

		carstore.close()

		infile = "carpark.txt"

		outfile = "carparkMod.txt"

		lines = []
		
		with open(infile, "r+") as f:
			for row in f:

				ines.append(row)

			f.close()

		lines(sort)

		with open(outfile, "w") as f1:

			with open(infile, "r+") as f:

				for line in lines:

					f1.write(line)

				f1.close()
			f.close()

		os.rename(outfile, infile)



		print("\n")

		main()

	elif choice == "2":

		'''Search specific data '''

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

		'''See all data '''

		carstore = open("carpark.txt", "r")
		
		carstore_display = carstore.read()
		
		#Car.defaultPrint()
		print(carstore_display)

		###############################################
		lines = []

		workingFile = "carpark.txt"

		with open(workingFile, "r+") as f:
			for row in f:
				#for i in range(4):
				lines.append(row)
		lines.sort()

		for line in lines:
			print(line)





		################################################

		print("\n")

		main()		

	elif choice == "4":

		''' Modify data ''' 
		
		carIdSearch = input('Enter the ID : ')
		#carParam = input('Enter the parameter: ')

		lines = []
		
		modlist = []

		infile = "carpark.txt"

		outfile = "carparkMod.txt"


		#outfile = "carparkMod.txt"


		with open(infile, "r+") as f:
			for row in f:

				lines.append(row)

			f.close()

		lines.sort()

		with open(outfile, "w") as f1:

			with open(infile, "r+") as f:

				for line in lines:

					if carIdSearch in line:
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

		modlist  = []

		with open(infile, "r+") as f:

			for row in f:

				lines.append(row)

			f.close()

		lines.sort()


		with open(outfile, "w") as f1:
			with open(infile, "r+") as f:

				for line in lines:

					if carIdSearch in line:

						print(line)
						
						deleteDesicion = input("Do you want to delete the record? Y/N: ")

						if deleteDesicion == 'y' or deleteDesicion == 'Y':

							if carIdSearch not in line:
						
								f1.write(line)
						
							break
						
						elif deleteDesicion == 'n' or deleteDesicion == 'N':
						
							main()
						
							break

						else:
							
							pass

		os.rename(outfile, infile)

	elif choice == "6":

		''' Exit ''' 
		
		print("Bye!")

		exit()

	else:
		
		print("Wrong button pressed.")
		
		main()

if __name__ == '__main__':
	main()
	
