

def scorecalc(score):
	if score <= 69 and score >= 60:
		grade = "D"
	if score <= 79 and score >= 70:
		grade = "C"
	if score <= 89 and score >= 80:
		grade = "B"
	if score <= 100 and score >=90:
		grade = "A"
	print "; Your grade is " + grade
	return;


print "Scores and Grades"

for num in range(1,10):
		print "Score: "
		score = input()
		answer = scorecalc(score)

print "End of the program. Bye!"