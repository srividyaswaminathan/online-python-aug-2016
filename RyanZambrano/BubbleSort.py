import random

# easy test case
a = [6, 5, 3, 1, 8, 7, 2, 4]

# 100 random #s between 0 and 10000
b = []
for x in xrange(0,100):
	b.append(random.randint(0,10000))

def BubbleSort(unordered):
	correct = 0
	while correct < len(unordered)-1:
		correct = 0
		for x in xrange(0,len(unordered)-1):
			if unordered[x] > unordered[x+1]:
				temp = unordered[x]
				unordered[x] = unordered[x+1]
				unordered[x+1] = temp
				correct = 0
			else:
				correct += 1
	return unordered

print BubbleSort(b)