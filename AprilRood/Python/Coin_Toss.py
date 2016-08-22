
import random
global headCount
global tailCount
headCount = 0
tailCount = 0

def cointoss():
	random_num = random.random()
	flip = round(random_num)
	if flip == 0:
		global tailCount
		tailCount = tailCount + 1
		return "tail"
	else:
		global headCount
		headCount = headCount + 1
		return "head"

print "Starting the program..."

for num in range(1,5000):
	

	print "Attempt #" + str(num) + ": Throwing a coin ... It's a " + cointoss() + "! ... Got " + str(headCount) + " head(s) so far and " + str(tailCount) + " tail(s) so far."

print "Ending the program, thank you!"	


			