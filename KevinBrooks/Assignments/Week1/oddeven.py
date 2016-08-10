def OddEven():
	output = "Number is {0}. This is an {1} number."
	identifier = ""
	for value in range(1,2001):
		identifier = ("odd","even") [value % 2 == 0]
		print output.format(value, identifier)

OddEven()