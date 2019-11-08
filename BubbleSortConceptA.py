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

def initializeList(oldCounter, oldSize, oldInputNumber):
	oldCounter /= 10
	numberList = []
	for i in range(oldSize):
		digit = int(oldInputNumber // oldCounter)
		digit = digit - ((int(digit // 10)) * 10)
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
	#Number container has been inititialized and is ready for sorting.
	print("Variable ready. Bubble Sorting now...")
 
	numberList = inputList
	sortedNumber = []
	
	sortingComplete = False
	
	while(sortingComplete == False):
	
	    length = len(numberList)
	    #print("Length = " + str(length))
	
	    spotA = length - 2
	    spotB = length - 1
	    
	    if(length == 2):
	    	a = numberList[spotA]
	    	b = numberList[spotB]
	    	if(a > b):
	    		c = numberList[spotA]
	    		numberList[spotA] = b
	    		numberList[spotB] = c
	    		sortedNumber.extend(numberList)
	    		sortingComplete = True
	    	#END final sort if
	    	
	    	else:
	    		sortedNumber.extend(numberList)
	    		sortingComplete = True
	    	#END normal case else
	    #END length check if
	    		    		    	
	    if(sortingComplete == False):
	        for j in range(length - 1):
	
	            a = numberList[spotA]
	            b = numberList[spotB]
	    
	            if(a > b):
	    	        c = numberList[spotA]
	    	        numberList[spotA] = b
	    	        numberList[spotB] = c
	            #END number switch if
	    
	            spotA -= 1
	            spotB -= 1
	        #END single iteration for loop
	    #END sorted-check if
	    
	    print("Value after partial sort: ")
	    printList(numberList)
	    
	    if(sortingComplete == False):
	        sortedNumber.append(numberList[0])
	        del numberList[0]
	        print("Old List: ")
	        printList(numberList)
	        print("New List: ")
	        printList(sortedNumber)
	    #END sorted-check if
	#END iterative while loop
	
	print("Fully Sorted Number: ")
	printList(sortedNumber)
	
#END main sorting function

#PROGRAM FLOW
userInput = input("Input a number to be sorted: ")

(counterTransfer, sizeTransfer, numberTransfer) = determineSize(int(userInput))
print("counterTransfer = " + str(counterTransfer))
print("sizeTransfer = " + str(sizeTransfer))
print("numberTransfer = " + str(numberTransfer))

output = initializeList(counterTransfer, sizeTransfer, numberTransfer)
print("Initialized List:", end=" ")
printList(output)

sort(initializeList(counterTransfer, sizeTransfer, numberTransfer))