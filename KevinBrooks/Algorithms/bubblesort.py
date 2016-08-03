import random
numbers = [int] 

for cntr in range(0,100):
	numbers.append(int(round(random.random() * 10000)))

def bubble_sort(arr):
	src_data = None
	dest_data = None
	last_index = len(arr)
	cntr = 0
	for first in range(last_index):
		for second in range(1, last_index):
			if arr[second - 1] > arr[second]:
				src_data = arr[second -1]
				dest_data = arr[second]
				arr[second - 1] = dest_data
				arr[second] = src_data
		
		last_index -= 1

bubble_sort(numbers)
print numbers
