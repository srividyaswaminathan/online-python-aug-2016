#Print all the integers from 1 to 255.

def print_integers():
	for i in range(1, 256):
		print "The integers are:", i
print_integers()
print "***********************************"

#Print all odd integers from 1 to 255.
def odd_integers():
	for i in range(1, 256, 2):
		print i
odd_integers()		
print "***********************************" 

#Print integers from 0 to 255, and with each integer print the sum so far.
def sum_integers():
	sum = 0
	for i in range(0, 256):
		sum = sum + i
		print "Sum so far is:", sum
sum_integers()		
print "***********************************" 
#Print all values in a given array.

def print_numbers_list(list_num):
	idex = 0
	for i in list_num:
		print "The number at {} index is {}".format(idex, i)
		idex +=1
print_numbers_list([2,3,345,35])
print "***********************************" 
#Print the largest element in a given array.
def max_in_list(array):
	print "The maximum number is:" ,max(array)
max_in_list([2,345,435,234,23])
print "***********************************" 
#Analyze an arrays values and print the average.
def print_average(array):
	avg = 0
	total = 0
	for i in array:
		total = total+i
	avg = total/len(array)
	print "Average val is ",avg
print_average([2,4,5])
print "***********************************" 
#Create and; return an array with odd integers from 1-255.
def return_odd_integers():
	odd_integers = []
	for i in range(1,256,2):
		odd_integers.append(i)
	return odd_integers	
print return_odd_integers()		
print "***********************************" 
#Given an array, square each value in the array.
def square(arr):
	new_arr = []
	for i in arr:
		new_arr.append(i*i)
	return new_arr
print square([5,7,9,11])	
print "***********************************" 
#Given an array, return the count that is greater than Y.
def count_greater(arr, Y):
	count = 0
	for i in range(0,len(arr)):
		if arr[i]>Y:
			count +=1
	return count
print "Count of numbers greater than Y is", count_greater([3,4,5,56,2], 50)
print "***********************************" 
#Given an array, set negative values to zero. 

def neg_to_zero(arr):
	for i in range(0, len(arr)):
		if arr[i]<0:
			arr[i] = 0
	return arr		
print neg_to_zero([3,4,-1,-2,-4])
print "***********************************" 
#Given an array, print max, min and average values. 
def max_min_avg(arr):
	total = 0
	maximum_num = max(arr)
	minimum_num = min(arr)
	for i in range(0, len(arr)):
		total = total+ arr[i] 
	average = float(total)/len(arr)
	print "Minimum number is:", minimum_num 
	print "maximum number is:",maximum_num
	print "averagevalue is:", average
print max_min_avg([2,4,5])
print "***********************************" 
#Given an array, replace negative values with Dojo
def replace_neg(arr):
	for i in range(0, len(arr)):
		if arr[i]<0:
			arr[i]= 'Dojo'
	return arr
print replace_neg([3,4,-2,-2,3,-5])	
print "***********************************" 
#Given an array, shift values forward by one, dropping the first value and leaving an extra '0' value at the end
def shift_forward(arr):
	for i in range(0, len(arr)-1):
		arr[i] = arr[i+1]
	arr[len(arr)-1]=0
	return arr
print shift_forward([3,4,5,1])	
print "***********************************" 