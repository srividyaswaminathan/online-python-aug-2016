
def average(lst):
	avg = 0 
	total = 0
	for i in lst:
		total += i
	avg = total/len(lst)
	print avg
	
average([1, 2, 5, 10, 255, 3])		