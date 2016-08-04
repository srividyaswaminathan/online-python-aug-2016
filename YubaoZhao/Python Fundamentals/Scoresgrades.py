#Assignment: Scores and Grades
# Create a program that prompts the user ten times for a test score between 60 and 100.
# Each time a score is generated, your program should display what is the grade of that score.
# Here is the grade table:
#
# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

def scores_grades():
    scorelist = []
    i = 0
    while i < 10:
        num = input("Enter a score(60-100):")
        if num >= 60 and num <=100:
            scorelist.append(num)
            i += 1
        else:
            print "Invalid score!"
            continue
    print "Scores and Grades"
    for score in scorelist:
        if score >= 90:
            grade = 'A'
        elif score >= 80:
            grade = 'B'
        elif score >= 70:
            grade = 'C'
        else:
            grade = 'D'
        print "Score: {}; Your grade is {}".format(score, grade)
    print "End of the program. Bye!"

scores_grades()
