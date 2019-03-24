from methods import (
	carCheck as carCheck,
	carIdCheck as carIdCheck,
	idRegEx as idRegEx)
import re

class Car(object):
	"""docstring for ClassName"""
	def __init__(self, carID, make, model, year, numberPlate, color, owner, place):
		self.carID = carID
		self.make = make
		self.model = model
		self.year = year
		self.numberPlate = numberPlate
		self.color = color
		self.owner = owner
		self.place = place	

	def getCarID(self):
		return self.carID

	def getMake(self):
		return self.make	

	def getModel(self):
		return self.model

	def getYear(self):
		return self.year

	def getNumberPlate(self):
		return self.numberPlate
	
	def getColor(self):
		return self.color

	def getOwner(self):
		return self.owner

	def getPlace(self):
		return self.place

	def setCarID(self, carID):
		self.carID = carID

	def setMake(self, make):
		self.make = make	

	def setModel(self, model):
		self.model = model
	
	def setYear(self, year):
		self.year = year

	def setNumberPlate(self, numberPlate):
		self.numberPlate = numberPlate

	def setColor(self, color):
		self.color = color

	def setOwner(self, owner):
		self.owner = owner

	def setPlace(self, place):
		self.place = place

	def __str__(self):
		return '{} {} {} {} {} {} {} {}\n'.format(
			self.carID,
			self.make,
			self.model, 
			self.year, 
			self.numberPlate, 
			self.color, 
			self.owner, 
			self.place)

	def carInput(file):
		
		carId = input("Enter carID in such a way:0000. Your input:  ")

		checkedCarId = idRegEx(carId)

		carId = str(checkedCarId)

		carNewId = carIdCheck(file, carId)

		carId = carNewId

		carMake = input("Make: ")
		
		carModel = input("Model: ")

		carYear = input("Year: ")

		carNumberPlate = input("Number Plate: ")

		carNewNumberPlate = carCheck(file, carNumberPlate)

		carNumberPlate = carNewNumberPlate

		carColor = input("Color: ")

		carOwner = input("Owner: ")

		carPlace = input("Place: ")

		#carNewPlace = carCheck(file, carPlace)

		#carPlace = carNewPlace

		carInCarPark = Car(
			carID = carId,
			make = carMake, 
			model = carModel, 
			year = carYear, 
			numberPlate = carNumberPlate, 
			color = carColor, 
			owner = carOwner, 
			place = carPlace)		

		return carInCarPark

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

'''dListZero = DoublyLinkedList()

dListOne = DoublyLinkedList()

dListTwo = DoublyLinkedList()

dListThree = DoublyLinkedList()

dListFour = DoublyLinkedList()

dListFive = DoublyLinkedList()

dListSix = DoublyLinkedList()

dListSeven = DoublyLinkedList()

dListEight = DoublyLinkedList()

dListNine = DoublyLinkedList()'''

#dList = [dListZero, dListOne, dListTwo, dListThree, dListFour, dListFive, dListSix, dListSeven, dListEight, dListNine]


