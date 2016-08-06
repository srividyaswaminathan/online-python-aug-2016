import random
head_count = 0
tail_count = 0

for x in range(1, 5001):
	random_num = random.random()
	rounded_num = round(random_num)
	if rounded_num == 1 :
		print ("Throwing a coin... It's a Head! ...Got {} Head(s) so far and {} Tail(s)").format(head_count, tail_count)
		head_count += 1
	elif rounded_num == 0 :
		print ("Throwing a coin... It's a Tail! ...Got {} Head(s) so far and {} Tail(s)").format(head_count, tail_count)
		tail_count += 1
