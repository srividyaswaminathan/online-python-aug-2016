# Assignment: Sum List
# Create a program that prints the sum of all the values in the list:

a = [1, 2, 5, 10, 255, 3]

def sum_list(arr):
    sum = arr[0]
    for value in arr[1:]:
        sum+=value
    return sum

print sum_list(a)
