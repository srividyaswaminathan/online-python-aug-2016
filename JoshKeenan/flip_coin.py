from random import random
def coin_flip():
		head_count = 0
		tail_count = 0
		for x in range(1, 5001):
			random_num = round(random())
			# random_num = round(random_num)
			if random_num == 1 :
				head_count += 1
				head_tail = "Head"
			elif random_num == 0 :
				tail_count += 1
				head_tail = "Tail"
			print ("Throwing a coin... It's a {}! ...Got {} Head(s) so far and {} Tail(s)").format(head_tail,head_count,tail_count)

coin_flip()