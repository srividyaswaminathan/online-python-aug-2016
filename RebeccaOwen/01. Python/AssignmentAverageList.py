# Pajama Programmer
# Coding Dojo - July 5 Online Flex
# 2-August-2016
# Assignment: Average List
# Create a program that prints the average of the values in the list: a = [1, 2, 5, 10, 255, 3]

def avg_list(a):
    total = 0
    for num in a:
        total+=num
    return total/len(a)

a = [1, 2, 5, 10, 255, 3]
print avg_list(a)
