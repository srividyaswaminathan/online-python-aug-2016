# Pajama Programmer
# Coding Dojo - July 5 Online Flex
# 2-August-2016
# Assignment: Sum List
# Create a program that prints the sum of all the values in the list: a = [1, 2, 5, 10, 255, 3]

def sum_list(a):
    total = 0
    for num in a:
        total+=num
    return total

a = [1, 2, 5, 10, 255, 3]
print sum_list(a)
