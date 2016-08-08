import random
import itertools

a = [170, 45, 75, 90, 802, 2, 24, 66]

b = []
for x in xrange(0,100):
	b.append(random.randint(0,10000))


def radixSort(unsorted):
	print 'Original list:\n', unsorted
	
	maxlen = 0
	for x in xrange(0,len(unsorted)):
		unsorted[x] = str(unsorted[x])	# int -> str for len()
		if len(unsorted[x]) > maxlen:	# maxlen to know how many digits to iterate through
			maxlen = len(unsorted[x])
	
	for y in xrange(0,maxlen):
		buckets = {'0':[], '1':[], '2':[], '3':[], '4':[], '5':[], '6':[], '7':[], '8':[], '9':[]} 
		for x in xrange(0,len(unsorted)):
			if ((len(unsorted[x])-1)-y) >= 0:
				if unsorted[x][(len(unsorted[x])-1)-y] in buckets.keys():
					buckets[unsorted[x][(len(unsorted[x])-1)-y]].append(unsorted[x])
			else:
				buckets['0'].append(unsorted[x])
		unsorted = [] 
		for z in xrange(0,10):
			if str(z) in buckets.keys():
				unsorted.append(buckets[str(z)])
		unsorted = list(itertools.chain(*unsorted))
	
	for x in xrange(0,len(unsorted)):
		unsorted[x] = int(unsorted[x])
	print 'Sorted list:\n', unsorted


radixSort(b)

#################
# print str(a[0])
# print str(a[0])[0]
# print str(a[0])[len(str(a[0]))-1]

# num = str(a[0])
# print num
# print num[0]
# print num[len(num)-1]

#################
# 	a = [170, 45, 75, 90, 802, 2, 24, 66]

# 	last
# 	0 = [170, 90]
# 	2 = [802, 2]
# 	4 = [24]
#	5 = [45, 75]
# 	6 = [66]

# 	2nd to last
# 	0 / IndexError? = [802, 2]
# 	2 = [24]
# 	4 = [45]
# 	6 = [66]
# 	7 = [170, 75]
# 	9 = [90]

# 	3rd to last
# 	0/IE? = [2,24,45,66,75,90]
# 	1 = [170]
# 	8 = [802]

# 	merge -> [2,24,45,66,75,90,170,802]