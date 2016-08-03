a = [1, 2, 5, 10, 255, 3]

def sumList(a):
	total = 0
	for x in range(0,len(a)-1):
		total += a[x];
	print total

sumList(a)