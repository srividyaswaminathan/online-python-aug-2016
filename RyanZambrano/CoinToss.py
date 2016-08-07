import random

def coinToss():
	head_total = 0
	tail_total = 0
	for x in xrange(0,5000):
		rand = random.random()
		rounded = round(rand)
		if rounded == 0:
			head_total += 1
			side = "head"
		elif rounded == 1:
			tail_total += 1
			side = "tail"
		print "Attempt #" + str(x+1) + ": Throwing a coin... it's a " + side + "! ... Got " + str(head_total) + " head(s) so far and " + str(tail_total) + "tail(s) so far"
	print "Ending the program, thank you!"
	
coinToss()