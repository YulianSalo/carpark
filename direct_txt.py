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



#dList = [dListZero, dListOne, dListTwo, dListThree, dListFour, dListFive, dListSix, dListSeven, dListEight, dListNine]

def main():

	menu()

	choice  = (input("Your choice:"))

	print("\n")

	if choice == "1":

		'''Input data '''

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

			dList[i].printList(dList[i].head)

		carstore.close()

		print("\n")

		dList = []

		main()

	elif choice == "2":

		'''Search specific data '''

		dList = [dListZero, dListOne, dListTwo, dListThree, dListFour, dListFive, dListSix, dListSeven, dListEight, dListNine]

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

		carIdSearch = input('Enter the search parameter: ')
	
		with open('carpark.txt', "r+") as f:
	
			for row in f:
		#for i in range(4):

				if row[3] == carIdSearch[3] and carIdSearch in row:

					for i in range(len(dList)):

						dList[i].push(row)

						dList[i].printList(dList[i].head)

						break

		dList = []

		main()
    	
	elif choice == "3":

		'''Read all data'''

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

		with open('carpark.txt', "r+") as f:
	
			for row in f:

				for i in range(len(dList)):

					if row[3] == str(i):

						dList[i].push(row)

			f.close()

		for i in range(len(dList)):
				
			dList[i].printList(dList[i].head)



		print("\n")

		dlist = []

		main()		

	elif choice == "4":

		''' Modify data ''' 

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
		
		carIdSearch = input('Enter the ID : ')

		modlist = []

		lines = []

		infile = "carpark.txt"

		with open('carpark.txt', "r+") as f:

			for row in f:

				for i in range(len(dList)):

					if row[3] == str(i):

						lines.append(row)

			f.close()

		with open(infile, "w+") as f:

			for line in lines:

				if carIdSearch in line:
					
					print(line)

					modlist.append(input("Field to modify: "))
					
					newfield = input("New data: ")

				for word in modlist:
					
					line = line.replace(word, newfield )
				
				f.write(line)

			f.close()

		dList = []



		'''for i in range(len(dList)):
				
			dList[i].printList(dList[i].head)

		with open(infile, "r+") as f:
	
			for row in f:
		#for i in range(4):

				if row[3] == carIdSearch[3]:

					lines.append(row)

			f.close()
		
		for i in range(len(dList)):

			#for j in range(len(dList[i])):

			if type(dList[i].head) is not None:

				#tmp = (pridList[i].head)
				
				tmp = str(dList[i].printList(dList[i].head))

				lines.append(tmp)

		print (lines)

		if carIdSearch in tmpString:

			print(dList[i].getNodeData(dList[i].head))

			dList[i].deleteNode(dList[i].head) 

			modField = input("Field to modify: ")

			newField = input("New data: ")

			tmp = str(dList[i].getNodeData(dList[i].head))

			tmp = tmp.replace(modField, newField)

			dList[i].push(tmp)

			#dList[i].printList(dList[i].head)

			#dList[i] = str(dList[i].replace(modField, newField))


		with open('carpark.txt', "r+") as f:
					
			for i in range(len(dList)):

				tmp = str(dList[i].getNodeData(dList[i].head))

				f.write(tmp)

				#f.close()

			f.close()'''

		main()

	elif choice == "5":

		''' Delete data '''

		#dList = [dListZero, dListOne, dListTwo, dListThree, dListFour, dListFive, dListSix, dListSeven, dListEight, dListNine]

		infile = "carpark.txt"

		carIdSearch = input('Enter the ID : ')

		lines = []

		with open('carpark.txt', "r+") as f:

			for row in f:

				for i in range(len(dList)):

					if row[3] == str(i):

						lines.append(row)

			f.close()

		for line in lines:

			if carIdSearch in line:

				print(line)

				deleteDesicion = input("Do you want to delete the record? Y/N: ")

				if deleteDesicion == 'y' or deleteDesicion == 'Y':

					lines.remove(line)
					
					with open(infile, "w+") as f:

						for line in lines: 

							f.write(line)
				
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

	elif choice == "0":

		print("Programming God's mode is not implemented yet.")

		main()

	else:
		
		print("Wrong button pressed.")
		
		main()

if __name__ == '__main__':
	main()
	
