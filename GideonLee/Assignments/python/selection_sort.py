# Selection Sort
# Modify your code so that instead of just getting the minimum when doing the 
# linear scan, it gets BOTH the maximum and the minimum and swaps two values
# after each linear scan.

from random import randint
import time

def createRandList():
	arr = []
	for i in range(0, 100): 
		rand = randint(0, 10000)
		arr.append(rand)
	return arr

#This code should be approximately (N^2)/2
def selection_sort(arr):
	start = 0 
	end = len(arr)

	while start < len(arr):
		swapFront = 'false'
		swapEnd = 'false' 
		smallest = arr[start]
		largest = arr[end-1]
		for i in range(start+1, end):
			#iterate through the array and find the smallest value
			#if one is found, set swapFront to 'true'
			if smallest > arr[i]:
				smallest = arr[i]
				indexMin = i
				swapFront = 'true'
			#iterate through the array and find the largest value
			#if one is found, set swapEnd to 'true'
			if largest < arr[i]:
				largest = arr[i]
				indexMax = i
				swapEnd = 'true'
		#if either swaps are set to 'true', perform respective swap
		if swapFront == 'true':
			temp = arr[start]
			arr[start] = smallest
			arr[indexMin] = temp
		#if swapEnd is performed, reduce the max size of the array by 
		#shrinking the search by 1 index since the largest digit will 
		#be set in place.  
		if swapEnd == 'true':
			temp = arr[end-1]
			arr[end-1] = largest
			arr[indexMax] = temp
			end -= 1
		start += 1
	return arr

test = createRandList()	

start_time1 = time.clock()
print selection_sort(test)

# Hey Charlie, is this the best way to go about checking the time/efficiency of my code? 
print '\nThis took:', time.clock() - start_time1, 'seconds'