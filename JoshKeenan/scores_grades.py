grade1 = input("Please enter Percent correct between 60 and 100: ")
grade2 = input("Please enter Percent correct between 60 and 100: ")
grade3 = input("Please enter Percent correct between 60 and 100: ")
grade4 = input("Please enter Percent correct between 60 and 100: ")
grade5 = input("Please enter Percent correct between 60 and 100: ")
grade6 = input("Please enter Percent correct between 60 and 100: ")
grade7 = input("Please enter Percent correct between 60 and 100: ")
grade8 = input("Please enter Percent correct between 60 and 100: ")
grade9 = input("Please enter Percent correct between 60 and 100: ")
grade10 = input("Please enter Percent correct between 60 and 100: ")

grade_list = [grade1,grade2,grade3,grade4,grade5,grade6,grade7,grade8,grade9,grade10]

print 

for number in grade_list:
	if number > 90 and number < 101:
		print ("Score: %s; Your Grade is A") % number
	elif number > 80 and number < 90:
		print ("Score: %s; Your Grade is B") % number
	elif number > 70 and number < 80:
		print ("Score: %s; Your Grade is C") % number
	elif number > 60 and number < 70:
		print ("Score: %s; Your Grade is D") % number
	else:
		print("End of Program.")