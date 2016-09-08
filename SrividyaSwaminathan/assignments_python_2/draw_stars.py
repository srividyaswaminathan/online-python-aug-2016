#Create a function called  draw_stars() that takes a list of numbers and prints out  *.

def draw_stars(lst):
	new_list = []
	for i in lst:
		print i* "*"
		
print draw_stars([2,4,5])

# Modify the function above. Allow a list containing integers and strings to be passed to the  draw_stars() function. When a string is passed, instead of  displaying *,
# display the first letter of the string according to the example below. You may use the .lower() string method for this part.

def modify_draw_stars(lst):
	for i in lst:
		if type(i)==str:
			print len(i)*i[0].lower()
		elif type(i)==int:
			print i * "*"

print modify_draw_stars(['Hello', 3, 'tom'])

