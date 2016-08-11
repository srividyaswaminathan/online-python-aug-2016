a = [1,2,5,10,255,3]

def SumValues(arr):
	total = 0
	for value in a:
		total += value

	return total

print "Sum = " + str(SumValues(a))