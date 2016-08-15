import random

def radix_sort(arr, index):
	buckets = [list() for new_list in range(10)]
	for i in range(len(arr)):
		buckets[int(str(arr[i]).zfill(10)[index : index + 1])].append(arr[i])
	
	arr = []
	for i in range(len(buckets)):
		for j in range(len(buckets[i])):
			arr.append(buckets[i][j])
	
	if index > 0:
		index -= 1
		arr = radix_sort(arr, index)	

	return arr


arr = []

for i in range(100):
	arr.append(int(round(random.random() * 100)))

arr = radix_sort(arr,9)

print arr