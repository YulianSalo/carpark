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

class Node: 

	def __init__(self, data):

		self.data = data  
	
		self.next = None
	
		self.prev = None

	def __str__(self, data):
	
		return self.data

class DoublyLinkedList: 

	def __init__(self): 
	
		self.head = None


	def deleteNode(self, dele): 

		if self.head is None or dele is None: 
			
			return 

		if self.head == dele:
			
			self.head = dele.next

		if dele.next is not None: 
			
			dele.next.prev = dele.prev 

		if dele.prev is not None: 
			
			dele.prev.next = dele.next

		gc.collect() 


	# Given a reference to the head of a list and an 
	# integer, inserts a new node on the front of list 
	def push(self, new_data): 

		# 1. Allocates node 
		# 2. Put the data in it 
		new_node = Node(new_data) 

		# 3. Make next of new node as head and 
		# previous as None (already None) 
		new_node.next = self.head 

		# 4. change prev of head node to new_node 
		if self.head is not None: 
		    self.head.prev = new_node 

		# 5. move the head to point to the new node 
		self.head = new_node 


	def printList(self, node): 
		
		while(node is not None): 
		
			print (node.data) 
		
			node = node.next

	def getNodeData(self, node):

		 data = node.data

		 return data

dListZero = DoublyLinkedList()

dListOne = DoublyLinkedList()

dListTwo = DoublyLinkedList()

dListThree = DoublyLinkedList()

dListFour = DoublyLinkedList()

dListFive = DoublyLinkedList()

dListSix = DoublyLinkedList()

dListSeven = DoublyLinkedList()

dListEight = DoublyLinkedList()

dListNine = DoublyLinkedList()

dList = [dListZero, dListOne, dListTwo, dListThree, dListFour, dListFive, dListSix, dListSeven, dListEight, dListNine]
  


def main():

	menu()

	choice  = (input("Your choice:"))

	print("\n")

	if choice == "1":

		'''Input data '''

		if not os.path.exists("carpark.txt"):

			carstore = open("carpark.txt", "w+")

		else:

			carstore = open("carpark.txt", "a")

		carInCarPark = Car.carInput()

		getCarId = str(carInCarPark.getCarID())

		for i in range(len(dList)):

			if getCarId[-1] == str(i):

				dList[i].push(str(carInCarPark))

				tmp = dList[i].getNodeData(dList[i].head)

				print(type(tmp))

				carstore.write(tmp)

			carstore.close()

			dList[i].printList(dList[i].head)

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

		#carstore = open("carpark.txt", "r")
		
		#carstore_display = carstore.read()
		
		#Car.defaultPrint()
		#print(carstore_display)

		lines = []

		sortId = []

		with open('carpark.txt', "r+") as f:
	
			for row in f:
		#for i in range(4):
				lines.append(row)

		for line in lines:
	
			for i in range(len(line)):
			
				gotId = line[3]

			sortId.append(gotId)



		for line in range(len(lines)):


			#print(lines[line], int(sortId[line]))

			for i in range(len(dList)):

				if int(sortId[line]) == i:

					dList[i].push(lines[line])


		for i in range(len(dList)):
				
			dList[i].printList(dList[i].head)



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
	
