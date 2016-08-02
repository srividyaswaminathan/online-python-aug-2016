arr = ["the", "array", ", do it now!"]
value = "Test"

arr.insert(0, value)

print "*********Insert Value**********"
print "Value = " + value
print "Arr after insert: " , arr
print "Join: " + " ".join(arr)

def RemoveFirst(arr):
	if len(arr) == 0:
		return ""

	first = arr[0]
	index = 1;
	while index < len(arr):
		arr[index -1] = arr[index]
		index+=1

	arr.pop()

	return first

print "**********Pop and Return*************"
print "Array Before Pop = " , arr
print "First Value = " , RemoveFirst(arr)
print "Array After Pop = " , arr

arr.insert(0, value)

print "**********Insert At*************"
print "Arrary After Insert = " , arr
