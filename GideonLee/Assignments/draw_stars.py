# Stars
# Part 1: 
# Create a function called draw_stars() that takes a list of numbers and print out *.

# Part 2: 
# Modify the function above. Allow a list containing integers and strings to be passed to the  
# draw_stars() function. When a string is passed, instead of  displaying *, display the first 
# letter of the string according to the example below. You may use the .lower() string method for this part.

x = [4, 6, 1, 'Gideon', 3, 'craig', 5, 7, 'samantha', 25] 

def draw_stars(arr):
	for i in range(len(arr)):
		if type(arr[i]) == int:
			print "*" * arr[i]
		else: 
			print arr[i][0] * len(arr[i])

draw_stars(x)