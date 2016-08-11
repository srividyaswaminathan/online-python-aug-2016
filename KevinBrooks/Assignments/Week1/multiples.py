index = 1
output = ""

print "*********Odds**************"
for index in range(1,1000):
	if index % 2 != 0:
		output += str(index) + ","

	index += 1
else:
	print output[:-1]


output = ""
print "*********Multiples of 5**************"

for index in range(5,1001):
	if index % 5 == 0:
		output += str(index) + ","
else:
	print output[:-1]