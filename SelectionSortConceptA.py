#DEFINING FUNCTIONS
def determineSize(inputNumber):
	size = 0
	counter = 1
	sizeDetermined = False
	while sizeDetermined == False:
		check = inputNumber / counter
		if check < 1:
			sizeDetermined = True
		else:
			size += 1
			counter *= 10
	#END size determination while
	print("There are " + str(size) + " digits in the number you entered...")
	return counter, size, inputNumber
#END  size determination function

def initializeList(oldCounter, oldSize, oldInputNumber, initialized):
	oldCounter /= 10
	numberList = []
	for i in range(oldSize):
		digit = int(oldInputNumber // oldCounter)
		digit = digit - ((int(digit // 10)) * 10)
		if(initialized == False):
			print("Digit = " + str(digit))
		numberList.append(int(digit))
		if oldCounter != 1:
			oldCounter /= 10
		#END counter_is_not_equal_to_one_check if
	#END numberList initialization for loop
	return numberList
#END list initialization function

def printList(inputList):
	for number in inputList:
		print(number, end=' ')
	#END list printing for loop
	print("\n")
#END numberList printing function

def sort(inputList):
	print("Sorting Now...")
	printList(inputList)
#END sorting function

#PROGRAM FLOW
userInput = input("Input a number to be selection sorted: ")

(counterTransfer, sizeTransfer, numberTransfer) = determineSize(int(userInput))
print("counterTransfer = " + str(counterTransfer))
print("sizeTransfer = " + str(sizeTransfer))
print("numberTransfer = " + str(numberTransfer))

output = initializeList(counterTransfer, sizeTransfer, numberTransfer, False)
print("Initialized List:", end=" ")
printList(output)

sort(initializeList(counterTransfer, sizeTransfer, numberTransfer, True))