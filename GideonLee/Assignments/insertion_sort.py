#Insertion Sort
from random import randint
import time

def createRandList(listSize, min, max):
	arr = []
	for i in range(0, listSize):
		arr.append(randint(min, max))
	return arr
	
test = createRandList(100, 0, 10000)

def insertion_sort(arr):
	i = 0	
	while i < len(arr): 
		last = i
		j = i+1
		while j > last:
			if j < len(arr):
				if arr[j] < arr[last]:
					temp = arr[j]
					arr[j] = arr[last]
					arr[last] = temp
			j -= 1
			if last != 0:
				last -= 1
		i += 1
	return arr

start_time = time.clock()
print insertion_sort(test)
print '\nThis took:', time.clock() - start_time, 'seconds'