# had trouble making the "Your grade is ... print on the same line as the input"

def ScoresAndGrades():
	x = 0
	print 'Scores And Grades'
	while x < 10:
		score = raw_input('Score: ')
		if 99 >= int(score) >= 90:
			print 'Your grade is an A.'
		if 89 >= int(score) >= 80:
			print 'Your grade is a B.'	
		if 79 >= int(score) >= 70:
			print 'Your grade is a C.'
		if 69 >= int(score) >= 60:
			print 'Your grade is a D.'
		if 59 >= int(score):
			print 'You have failed.'
		x += 1
	print 'End of the program. Bye!'	
	
ScoresAndGrades()