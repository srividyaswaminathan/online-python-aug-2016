import csv

with open('us-500.csv', 'rU') as infile:
	reader = csv.DictReader(infile)
	users = {}
	for row in reader:
		key = row["first_name"] + " " + row["last_name"]
		users[key] = row	


for key, value in users.iteritems():
	print key
	for field, data in value.iteritems():
		print field + " : " + data
	print "-" * 20
