#Create a program that prompts the user ten times for a test score between 60 and 100. Each time a score is generated, your program should display what is the grade of that score. Here is the grade table:
#Score: 60 - 69; Grade - D
#Score: 70 - 79; Grade - C
#Score: 80 - 89; Grade - B
#Score: 90 - 100; Grade - A

score = []

def score_grades():
	for i in range(0,10):
		score.append(int(raw_input("Enter your grade between 60 and 100")))

		if(score[i]>=60 and score[i]<70):
			print "Score:" ,str(score[i])  + " your grade is D"
		elif(score[i]>=70 and score[i]<80): 
			print "Score:" , str(score[i])   +" your grade is C"
		elif(score[i]>=80 and score[i]<90):
			print "Score:" ,str(score[i]) + " your grade is B"
		elif(score[i]>=90 and score[i]<=101):
			print "Score:", str(score[i]) +" your grade is A"	
		else:
			print "please enter a valid score"	
	print "End of program. Bye!"

score_grades()