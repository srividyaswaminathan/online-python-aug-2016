import random, datetime
numbers = [int] 

for cntr in range(0,10000):
	numbers.append(int(round(random.random() * 10000)))

def selection_sort(arr):
	cnt = 0
	src_temp = None
	dest_temp = None
	for first in range(len(arr)):
		smallest_index = -1
		largest_index = -1
		for second in range(first, len(arr)):
			cnt += 1
			if smallest_index == -1 or arr[second] < arr[smallest_index]:
				smallest_index = second 
			elif largest_index == -1 or arr[second] > arr[largest_index]:
				largest_index = second

		src_temp = arr[first]
		dest_temp = arr[smallest_index]
		arr[first] = dest_temp
		arr[smallest_index] = src_temp
		src_temp = arr[smallest_index]
		dest_temp = arr[largest_index]
		arr[smallest_index] = dest_temp
		arr[largest_index] = src_temp

	return cnt

start = datetime.datetime.now()
count = selection_sort(numbers)
elapsed = datetime.datetime.now() - start
print "Execution Time: " + str(elapsed)
print "Count Iterations: " + str(count)
#print numbers
