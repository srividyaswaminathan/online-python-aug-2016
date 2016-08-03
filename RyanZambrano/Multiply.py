a = [2,4,10,16]

def multiply(a, n):
	multiplied = []
	for x in xrange(0,len(a)):
		multiplied.append(a[x] * n)
	return multiplied
	

b = multiply(a, 5)
print b