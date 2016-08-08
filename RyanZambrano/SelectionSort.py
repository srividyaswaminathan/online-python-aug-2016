import random

a = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]

b = []
for x in xrange(0,100):
	b.append(random.randint(0,10000))


def SelectionSort(unordered):
	y = 0
	while y < len(unordered):
		small = unordered[y]
		for x in xrange(y,len(unordered)):
			if unordered[x] <= small: # find smallest and its index
				small = unordered[x]
				small_index = x
		# right after each pass:
		temp = unordered[y] # where small will go's # is made temp
		unordered[y] = small # small put in place
		unordered[small_index] = temp # where small was is now first one's #
		y += 1 # change position of next smallest / shorten amount of list needed to sort through
	return unordered


print SelectionSort(b)