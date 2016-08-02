# MULTIPLES

# PART I
# Create a program that prints all the odd numbers from 1 to 1000. Use the for loop and don't use any array to do this exercise.

def print_odds():
    for num in range(1,1001):
    	if num % 2 == 1:
		print num

# print_odds()

# Part II
# Create another program that prints all the multiples of 5 from 5 to 1,000,000.
def print_mults():
    # Specify the step by giving range() a third parameter
    for mult in range(5, 1000005, 5):
        print mult

# print_mults()
