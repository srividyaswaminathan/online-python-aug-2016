def Scores_and_Grades(grade):
	print 'Scores and Grades'
	if grade in range (90, 100):
		print 'Score:' + str(grade) + "; Your grade is A"
	if grade in range (80, 89):
		print 'Score:' + str(grade) + "; Your grade is B"
  	if grade in range (70, 79):
	 	print 'Score:' + str(grade) + "; Your grade is C"
  	if grade in range (60, 69):
		print 'Score:' + str(grade) + "; Your grade is D"
	else:
		print 'End of the Program. Bye!'
print Scores_and_Grades(60)
print Scores_and_Grades(99)
print Scores_and_Grades(75)
