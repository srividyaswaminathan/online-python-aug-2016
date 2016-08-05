# Multiply, Create a function called 'multiply' that reads each value 
# in the list (e.g. a = [2, 4, 10, 16]) and returns a list where each 
# value has been multiplied by 5.

arr = [2, 4, 10, 16]
def multiply(arr):
	for i in range(len(arr)): 
		arr[i] = arr[i] * 5
	return arr

print multiply(arr)
