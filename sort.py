import os

lines = []

sortId = []

gotId = " "

workingFile = "carParkSort.txt"

with open(workingFile, "r+") as f:
	
	for row in f:
		#for i in range(4):
		lines.append(row)

print(len(lines))
	
for line in lines:
	
	for i in range(len(line)):
			
		gotId = line[0] + line[1] + line[2] + line[3]

	sortId.append(gotId)

sortId.sort()


with open("idList.txt", "w") as f1:

	with open(workingFile, "r+") as f:
	
		for i in range(len(sortId)):

			f1.write(sortId[i])

		f1.close()

	f.close()

print(sortId)

