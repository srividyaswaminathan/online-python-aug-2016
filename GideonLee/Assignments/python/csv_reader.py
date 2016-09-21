import csv

with open('us-500.csv', 'rU') as f:
	reader = csv.reader(f)
	legend = reader.next()
	for row in reader:
		print row[0] + ' ' + row[1]
		for index in range (0, len(legend)):
			print legend[index]	+ ': ' + row[index]
		print '---------------'