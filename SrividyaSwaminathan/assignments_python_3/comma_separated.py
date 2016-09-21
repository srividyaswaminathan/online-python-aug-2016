import csv

with open('us-500.csv', 'rU') as f:
	read_file = csv.reader(f)
	new_file = read_file.next()
	for row in read_file:
		print row[0] + " " + row[1]
		for i in range(2,12):
			print new_file[i], ":" ,row[i] 
		print "----------------------------------------------"