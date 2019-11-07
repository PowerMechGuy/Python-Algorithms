userInput = input("Input a number to be sorted: ")
num = int(userInput)

print("Setting up variables...")

#determine how many digits there are
sizeDetermined = False
size = 0
counter = 1

while sizeDetermined == False:
	check = num / counter
	if check < 1:
		sizeDetermined = True
	else:
		size += 1
		counter *= 10
#END size determination while

print("There are " + str(size) + " digits in the number you entered...")

numberList = []
sortedNumber = []
counter /= 10 

for i in range(size):
	digit = int(num // counter)
	if i > 0:
		digit = digit - ((int(digit // 10)) * 10)
	numberList.append(int(digit))
	if counter != 1:
		counter /= 10
#END numberList initialization for loop

def printList():
	for number in numberList:
		print(number, end=' ')
	#END list printing for loop
#END numberList printing function

printList()

print("\n")	
	
#Number container has been inititialized and is ready for sorting.
print("Variable ready. Bubble Sorting now...")
#################################

def sort():
	#This function will sort the number
	#using bubble sort
	
	sorted = False
	
	length = len(numberList)
	
	print("Length of numberList variable: " + str(length))
	
	a = numberList[length - 2]
	b = numberList[length - 1]
	
	if a > b:
		c = numberList[length - 2]
		numberList[length - 2] = b
		numberList[length - 1] = c
	#END switch numbers if
	
	printList()
	
#END main sorting function

sort()