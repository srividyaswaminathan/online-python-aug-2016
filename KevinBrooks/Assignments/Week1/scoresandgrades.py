def PrintGrade(score):
	output = "Score: {0}; Your grade is {1}"
	grade = "E"

	try:
		score = int(score)
		if score > 59 and score < 70:
			grade = "D"
		elif score > 69 and score < 80:
			grade = "C"
		elif score > 79 and score < 90:
			grade = "B"
		elif score > 89:
			grade = "A"
	except Exception, e:
		score = "invalid score"
	
	print output.format(score, grade)

for index in range(0,10):
	value = raw_input("Please enter your score: ")
	PrintGrade(value)
