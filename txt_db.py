import os
from objects import Car as Car
from methods import menu as menu


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
	
