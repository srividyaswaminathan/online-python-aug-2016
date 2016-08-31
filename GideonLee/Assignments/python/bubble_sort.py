# Bubble Sort
from random import randint
import time

start_time = time.clock()

def createRandomList(): 
	arr = []
	for i in range(0, 100): 
		score = randint(0, 10000)
		arr.append(score)
	return arr
 
test = createRandomList()

def bubble_sort(arr):
	for outer in range(0, len(arr)):
		for inner in range(0, len(arr)):
			nextOne = inner + 1
			if nextOne < len(arr):
				if arr[inner] > arr[nextOne]:
					temp = arr[inner]
					arr[inner] = arr[nextOne]
					arr[nextOne] = temp
	return arr 

print bubble_sort(test)

print '\nThis took:', time.clock() - start_time, 'seconds'