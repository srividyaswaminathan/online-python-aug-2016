#Sum List, Create a program that prints the sum of all the values in the list:
a = [1, 2, 5, 10, 255, 3] 

#Using a for loop
def sum_list(arr):
	total = 0
	for index in range(0, len(arr)):
		total += arr[index]		
	print total

sum_list(a)


#Using a while loop
# total = 0
# index = 0
# while index < len(a):
# 	total = total + a[index]
# 	index = index + 1
# print total
