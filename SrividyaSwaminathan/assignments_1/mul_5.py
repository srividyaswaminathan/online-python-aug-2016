#Create a function called 'multiply' that reads each value in the list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

def multiply(a, b):
	new_list = []
	for i in a:
		print "i here is", i
		new_list.append(i*b)
	return new_list	


print multiply([2,4,5], 5)		

