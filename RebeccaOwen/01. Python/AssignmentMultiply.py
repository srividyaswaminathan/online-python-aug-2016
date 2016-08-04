# Pajama Programmer
# Coding Dojo - July 5 Online Flex
# 2-August-2016
# Assignment: Multiply
# Create a function called 'multiply' that reads each value in the list (e.g. a = [2, 4, 10, 16])
# and returns a list where each value has been multiplied by 5.

def mult_5(a):
    b = []
    for i in a:
        b += [i*5]
    return b
        
a = [2, 4, 10, 16]
print mult_5(a)
