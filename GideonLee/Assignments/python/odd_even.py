# Odd/Even, Create a function that counts from 1 to 2000. As it loops 
# through each number, have your program generate the number and 
# specify whether it's an odd or even number.

def odd_or_even():
	for i in range(1, 2001):
		if (i % 2 == 1):
			print 'Number is ' + str(i) +'. This is an odd number.'
		else:
			print 'Number is ' + str(i) + '. This is an even number.'

odd_or_even()