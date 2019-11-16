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
#END numberList printing functi

def sort(inputList):
	print("Sorting Now...")
	printList(inputList)
	
	sortedNumber = []
	
	sortingComplete = False
	
	while(sortingComplete == False):
		
		length = len(inputList)
		c = 0
		
		if(length == 2):
			spotA = 0
			spotB = 0
			a = inputList[spotA]
			b = inputList[spotB]
			
			if(a < b):
				c = inputList[spotA]
				inputList[spotA] = inputList[spotB]
				inputList[spotB] = c
			#END a_is_less_than_b if
			elif(b < a):
				c = inputList[spotB]
				inputList[spotB] = inputList[spotA]
				inputList[spotA] = c
			#END b_is_less_than_a elif
			
			sortedNumber.extend(inputList)
			print("Fully Sorted Number: ")
			printList(sortedNumber)
			sortingComplete = True
			
		#END length_equal_to_2 check if
		
		spotA = 0
		spotB = 1
		spotC = 0
		
		if(sortingComplete == False):
			for j in range(length - 1):
				a = inputList[spotA]
				b = inputList[spotB]
			
				if(a < b):
					c = a
					spotC = spotA
				#END a_is_less_b if
			
				elif(b < a):
					c = b
					spotC = spotB
				#END b_less_than_a elif
			
				spotA += 1
				spotB += 1
			#END length_-_1 for loop
		#END sortingComplete_equal_to_false_check if
		
		if(sortingComplete == False):
			print("c is equal to: " + str(c))
		
			d = inputList[0]
			inputList[0] = c
			inputList[spotC] = d
			sortedNumber.append(inputList[0])
			del inputList[0]
		
			print("Old List")
			printList(inputList)
			print("New List")
			printList(sortedNumber)
		#END sortingComplete_equal_to_false check if
	#END sorted_equals_false while loop
		

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