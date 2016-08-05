import random

a = [6, 5, 3, 1, 8, 7, 2, 4]

b = []
for x in xrange(0,100):
	b.append(random.randint(0,10000))

def InsertionSort(unsorted):
	for x in xrange(0,len(unsorted)):
		for y in xrange(x,0,-1):
			if unsorted[y-1] > unsorted[y]:
				temp = unsorted[y]
				unsorted[y] = unsorted[y-1]
				unsorted[y-1] = temp
	return unsorted				

print InsertionSort(b)




# for x in range length of string
# if x == 0 
# done
# if string[x-1] < string[x]
# done
# if string[x-1] > string[x]
	# temp = string[x]
	# string[x] = string [x-1]
	# string[x-1] = temp