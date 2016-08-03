a = [1, 2, 5, 10, 255, 3]

def avgList(a):
	total = 0
	avg = 0
	for x in range(0,len(a)-1):
		total += a[x];
	avg = total / len(a)
	print "avg: " + str(avg)

avgList(a)