a = [1,2,5,10,255,3]

def Average(arr):
	total = 0
	for value in a:
		total += value

	return total/len(arr)

print "Average = " + str(Average(a))