#Part I, Create a program that prints all the odd numbers from 1 to 1000. 
#Use the for loop and don't use array to do this exercise.
def print_all_odd():
	for count in range(1, 1000):
		if count % 2 == 1: 	
			print count

print_all_odd()

#This is the same solution using a while loop
# x = 1
# while x < 1000:
# 	print x
# 	x += 2


#Part II, Create another program that prints all the multiples of 5 from 
#5 to 1,000,000. 
def print_multiples_of_five():
	for count in range(5, 1000001, 5):
		print count

print_multiples_of_five()

#This is the same solution using a while loop
# x = 5
# while x <= 1000000:
# 	print x
# 	x += 5