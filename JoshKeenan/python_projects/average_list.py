def find_avg(list):
	sum = 0
	for x in list:
		sum += x
	avg = sum / len(list)
	print avg

find_avg([1, 2, 5, 10, 255, 3])