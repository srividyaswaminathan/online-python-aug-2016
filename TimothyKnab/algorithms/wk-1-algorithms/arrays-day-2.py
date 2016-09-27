# Arrays Day 2 Algorithm Challenges - solutions written in Python - Tim Knab, August 2016


### Remove At
# Given array and an index into array, remove and return the array value at that index. 
# Do this without using built-in array methods except `pop()`. Think of `PopFront(arr)` as equivalent to `RemoveAt(arr,0)`.

arr = [1, 2, 3, 4, 5]  # creates our array

def removeAt(arr, idx):		# creates a new function called removeAt with the parameters (arr, idx)
	x = arr[idx]			# creates a new variable called x which stores the value we want to pop
	arr.pop(idx)			# pop the value for the idx value of choice
	return x				# return x (note, if we tried to return arr[idx], our value would be off as our integer is already popped)

print removeAt(arr, 2)		# print our function with the array and idx value





###Swap Array Pairs
# Swap positions of successive pairs of values of given array. If length is odd, do not change final element. For `[1,2,3,4]`, return `[2,1,4,3]`. For `[false,true,42]`, return `[true,false,42]`.


arr = [1, 2, 3, 4, 5]

def swapArrayPairs(arr):
	for idx, val in enumerate(arr):
		if len(arr) % 2 == 0:
			arr[idx], arr[val] =  arr[val], arr[idx]
		else:
			arr[0], arr[1] = arr[1], arr[0]  # QUESTION 1: I know this is not the exact solution line but this is where I need something to evaluate len(arr)-1 and make sure we only swap pairs up to that point. Posted on Stack for some insight.
	return arr

print swapArrayPairs(arr)
# my algorithm above does not work properly for odd lengthed lists nor with strings, so I went to stackoverflow to learn some alternative approaches:



# Here's some insight on this algorithm from the Stack Overflow community:
arr2 = [1, 2, "this", "that", 3, 4, 5]

def swap_list_pairs(arr):
	# this goes through the length of the list in a range starting with 1 through the length ofthe list, in steps of two:
    for index in range(1, len(arr), 2):    
        arr[index-1], arr[index] = arr[index], arr[index-1]  # swaps each step-2 pair, 'index-1' prevents any index error
    return arr

print swap_list_pairs(arr2)




###Remove duplicates
scores = [10, 10, 9, 8, 7, 7, 6, 6, 5]


# note that the answer below came from research on Stack Overflow and I still need to fully get my head around the set() function
def removeDuplicates(arr):
	seen = set()   # make sure you fully understand the usage of set() here and what's happening
	uniq = []
	for x in scores:
		uniq.append(x)
		seen.add(x)
	return seen

print removeDuplicates(scores)  

# QUESTION 2: How can I remove the set() attribute that is added here in the output?



