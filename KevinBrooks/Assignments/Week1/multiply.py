a = [2,4,10,16]

def Multiply(arr, multiplier):
	newArr = [None] * len(arr)
	for index in range(len(arr)):
		newArr[index] = arr[index] * multiplier

	return newArr

print Multiply(a,5)