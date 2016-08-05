# Pajama Programmer
# Coding Dojo - July 5 Online Flex
# 2-August-2016
# Assignment: Odd / Even
# Create a function that counts from 1 to 2000. As it loops through each number,
# have your program generate the number and specify whether it's an odd or even number.

def odd_even(n=1000):
    for i in range(1,2000):
        string = 'Number is '+str(i)+'. This is an '
        if i%2==0:
            string += 'even number.'
        else:
            string += 'odd number.'
        print string
        

odd_even()
