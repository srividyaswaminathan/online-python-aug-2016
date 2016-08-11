import csv
with open ('us-500.csv','rU') as us500:
	reader = csv.reader(us500)
	headers = reader.next()
	# organize entries dict
	entries = {}
	for header in headers:
		entries[header] = []
	for row in reader:
		for header, info in zip(headers, row):
			entries[header].append(info)
	# print entries
	n= 0
	while n < len(entries['first_name']):
		for header in headers:
			print header+":" , entries[header][n]
		print '---------------'
		n += 1