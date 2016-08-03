# Coin Tosses, You're going to create a program that simulates tossing a 
# coin 5,000 times. Your program should display how many times the 
# head/tail appears.
import random

def coinToss():
	heads = 0
	tails = 0
	for i in range(0, 5001):		
		random_num = random.random()
		rounded_num = round(random_num)
		if rounded_num == 0:
			heads += 1
			print "Attempt #" + str(i) + ": Throwing a coin... it's a head! ... Got " + str(heads) + " head(s) so far and " + str(tails) + "tail(s) so far"
		else:
			tails += 1
			print "Attempt #" + str(i) + ": Throwing a coin... it's a tail! ... Got " + str(heads) + " head(s) so far and " + str(tails) + "tail(s) so far"
	print 'Ending the program, thank you!'

coinToss()