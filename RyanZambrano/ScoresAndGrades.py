def ScoresAndGrades():
	x = 0
	grade = ''
	print 'Scores And Grades'
	while x < 10:
		score = raw_input('Score: ')
		if 100 >= int(score) >= 90:
			grade = 'A'
		if 89 >= int(score) >= 80:
			grade = 'B'
		if 79 >= int(score) >= 70:
			grade = 'C'
		if 69 >= int(score) >= 60:
			grade = 'D'
		if 59 >= int(score):
			grade = 'F'
		print 'Your grade is an', grade
		x += 1
	print 'End of the program. Bye!'	
	
ScoresAndGrades()