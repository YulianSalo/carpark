import os

lines = []

sortId = []

gotId = " "

workingFile = "carpark.txt"

with open(workingFile, "r+") as f:
	for row in f:
		#for i in range(4):
		lines.append(row)
	'''for line in lines:
		for i in range(len(line)):
			gotId = line[0] + line[1] + line[2] + line[3]

		sortId.append(gotId)

print(sortId)

sortId.sort()

print(sortId)'''
lines.sort()
print(lines)
