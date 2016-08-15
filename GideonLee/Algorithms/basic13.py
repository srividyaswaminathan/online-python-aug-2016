# Print 1-255
def printAll():
	for i in range(1, 256):
		print i

# printAll()


# Print Odds 1-255
def printOdd():
	for i in range(1, 256, 2):
		print i

# printOdd()


# Print integers from 0 to 255, and with each integer print the sum so far.
def printIntAndSum(): 
	sum = 0
	for i in range(0, 256):
		sum += i
		print 'Integer: ' + str(i) + '. Current Sum:', sum
		 
# printIntAndSum()


# Iterate through a given array, printing each value.
arr = [10, 11, 12, 13, 14, 15]
def iterateAndPrint(arr):
	for i in arr:
		print i

# iterateAndPrint(arr)


# Find and Print Max
def printMax(arr):
	max = arr[0]
	for i in arr:
		if i > max:
			max = i
	print max

# printMax(arr)


# Get and Print Average
# Analyze an array's values and print the average.
def printAvg(arr):
	avg = 0
	for i in arr: 
		avg += float(i)
	print avg/len(arr)

# printAvg(arr)


# Array with Odds
# Create an array with all the odd integers between 1 and 255 (inclusive).
def createOddArray():
	arr = []
	for i in range(1, 256, 2):
		arr.append(i)
	return arr

# print createOddArray()


# Square each value in a given array, returning that same array with changed values.
def squareVales(arr):
	for i in range(0, len(arr)):
		arr[i] = arr[i] * arr[i]
	return arr

# print squareVales(arr)


# Given an array and a value Y, count and print the number of array values greater than Y.
def greaterThanY(arr, y):
	count = 0
	for i in arr:
		if i > y:
			print i
			count += 1
	print 'There are ' + str(count) + ' values greater than', y		

# greaterThanY(arr, 12)


# Zero Out Negative Numbers
arr = [-1, 10, -5, 20, -6, 30, -17, 40]
def zeroOut(arr):
	for i in range(0, len(arr)):
		if arr[i] < 0:
			arr[i] = 0
	return arr

# print zeroOut(arr)


# Max, Min, Average
# Given an array, print the max, min and average values for that array.
def findMinMaxAvg(arr):
	min = arr[0]
	max = arr[0]
	avg = 0
	for i in arr:
		if i > max:
			max = i
		elif i < min:
			min = i
		avg += float(i)
	print 'Min:', min
	print 'Max:', max
	print 'Average:', avg/len(arr)

# findMinMaxAvg(arr)


# Shift Array Values
# Given an array, move all values forward by one index, dropping the first and leaving a 0 value at the end.
arr = [10, 20, 30, 40, 50]
def shiftArrayValues(arr):
	for i in range(0, len(arr)):
		if i < len(arr)-1:
			arr[i] = arr[i+1]
	arr[len(arr)-1] = 0
	return arr

# print shiftArrayValues(arr)


# Given an array of numbers, replace any negative values with the string 'Dojo'.
arr = [-1, 10, -7, 20, -13, 30, -5, 40]
def replaceNegatives(arr):
	for i in range(0, len(arr)):
		if arr[i] < 0:
			arr[i] = 'Dojo'
	print arr

# replaceNegatives(arr)