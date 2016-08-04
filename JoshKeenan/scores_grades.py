score_list = []

for num in range(10):
	score_list.append(input("Please enter Percent correct between 60 and 100: "))

for score in score_list:
	if score >= 90:
		grade = "A"
	elif score >= 80 and score < 90:
		grade = "B"
	elif score >= 70 and score < 80:
		grade = "C"
	elif score < 70:
		grade = "D"

	print ("Score: {}: Your Grade is {}").format(score, grade)

print "End of program"
