# Pajama Programmer
# Coding Dojo - July 5 Online Flex
# 2-August-2016
# Assignment: Scores and Grades
# Create a program that prompts the user ten times for a test score between 60 and 100.
# Each time a score is generated, your program should display what is the grade of that score.
# Here is the grade table:
##Score: 60 - 69; Grade - D
##Score: 70 - 79; Grade - C
##Score: 80 - 89; Grade - B
##Score: 90 - 100; Grade - A

def score_to_grade(score):
    if score > 59 and score < 70:
        return 'D'
    if score > 69 and score < 80:
        return 'C'
    if score > 79 and score < 90:
        return 'B'
    if score > 89 and score < 101:
        return 'A'

print 'Score and Grades'
for i in range(10):
    print 'Score:',
    score = input()
    grade = score_to_grade(score)
    print ' Your grade is', grade

print 'End of program. Bye!'

