# Scores and Grades, Create a program that prompts the user ten times for
# a test score between 60 and 100. Each time a score is generated, your 
# program should display what is the grade of that score. Here is the 
# grade table:

def scores_and_grades():
		
	for i in range(0, 10):
		score = input()
		if score >= 60 and score < 70:
			print 'Score: ' + str(score) + '; Your grade is D'
		elif score >= 70 and score < 80:
			print 'Score: ' + str(score) + '; Your grade is C'
		elif score >= 80 and score < 90:
			print 'Score: ' + str(score) + '; Your grade is B'
		elif score >= 90 and score <= 100: 
			print 'Score ' + str(score) + '; Your grade is A'
		else:
			print 'Score ' + str(score) + '; You failed!'
	print 'End of the program. Bye!'

scores_and_grades()