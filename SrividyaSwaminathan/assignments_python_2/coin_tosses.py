# pseudo code : generate a random number 
#loop through a newly created list that loops from 1 - 5001
#write a function that calls if condition for random number 0 or 1 , if 0 its heads , if 1 its tails
#write a function that will count the number of heads and tails 


import random

def toss():
	random_num = random.random()
	random_round = round(random_num)
	return random_round	


head = 0 
tail =0
for i in range(1, 5001):	
	if (toss()==1):
		head += 1
		text = "head"
	else:	
		tail +=1
		text = "tails"
	print " Attempt #{} Throwing a coin..Its a {}... Got {} heads so far and {} tails so far".format(i, text, head, tail)
