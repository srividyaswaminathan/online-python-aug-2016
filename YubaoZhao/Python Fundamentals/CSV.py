# Optional Assignment: CSV

import csv

reader = csv.reader(open('us-500.csv', 'rU'))
first_row = reader.next()
for row in reader:
    print row[0],row[1]
    for idx in range(len(row)):
        print "{}: {}".format(first_row[idx],row[idx])
    print "-"*40
