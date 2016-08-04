# Write a function that collects a bunch of inputs
def collect_inputs(times):
    scores = []
    for i in range(times):
        scores.append(input("Enter a score:"))

    # Scores is a list of numbers
    return scores
    # Run a loop based on the times variable
    # Collect an input each time

def print_scores(scores):
    print "Scores and Grades: "
    for score in scores:
        # This will print out a sentence
        print_score_string(score)
    print "End of program"

# Write a function that can generate score string
def print_score_string(score):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    else:
        grade = 'D'
    print "Score: {} .... Your grade is {}".format(score, grade)

print_scores( collect_inputs(10) )
