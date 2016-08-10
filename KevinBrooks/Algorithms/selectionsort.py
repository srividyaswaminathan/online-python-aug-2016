import random, datetime
numbers = [int] 

for cntr in range(0,100):
	numbers.append(int(round(random.random() * 10000)))

def selection_sort(arr):
	src_temp = None
	dest_temp = None
	for first in range(len(arr)):
		smallest_index = -1
		for second in range(first, len(arr)):
			if smallest_index == None or arr[second] < arr[smallest_index]:
				smallest_index = second 

		src_temp = arr[first]
		dest_temp = arr[smallest_index]
		arr[first] = dest_temp
		arr[smallest_index] = src_temp


start = datetime.datetime.now()
selection_sort(numbers)
elapsed = datetime.datetime.now() - start
print "Execution Time: " + str(elapsed)
print numbers
