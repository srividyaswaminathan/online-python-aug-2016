import csv
print csv
# import pprint
# pp = pprint.PrettyPrinter()
#
# MAKE SURE YOU HAVE ACCESS TO THE FILE
with open('us-500.csv', 'rU') as csv_file:
    reader = csv.reader(csv_file)
    keys = reader.next()
    for data in reader:
        print "{} {}".format(data[0], data[1])
        for idx in range(len(keys)):
            print "{}: {}".format(keys[idx], data[idx])
        print "\n _ _ _ _ _ _ _ _ _ _ _ \n"
