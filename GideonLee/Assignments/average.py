#Average List, Create a program that prints the average of the values in the list: 
a = [1, 2, 5, 10, 255, 3]

def averageUsingForLoop(arr):
	total = 0
	for i in arr:
		total += i
	total /= len(arr)
	print total

averageUsingForLoop(a);


#Using a while loop

# def averageUsingWhileLoop(arr):
# 	i = 0
# 	total = 0
# 	while i < len(arr):
# 		total += a[i]
# 		i+=1
# 	total /= len(arr)
# 	print total

# averageUsingWhileLoop(a)