import random, datetime
numbers = [int] 

for cntr in range(0,100):
	numbers.append(int(round(random.random() * 10000)))

def bubble_sort(arr):
	src_data = None
	dest_data = None
	last_index = len(arr)
	for first in range(last_index):
		for second in range(1, last_index):
			if arr[second - 1] > arr[second]:
				src_data = arr[second -1]
				dest_data = arr[second]
				arr[second - 1] = dest_data
				arr[second] = src_data
		
		last_index -= 1

start = datetime.datetime.now()
bubble_sort(numbers)
elapsed = datetime.datetime.now() - start
print "Execution Time: " + str(elapsed)
print numbers
