import random

def TossCoin():
	return round(random.random()) == 1

output = "Attempt #{0}: Throwing a coin... It's a {1}! ... Got {2} head(s) so far and {3} tail(s) so far"
cntHeads = 0
cntTails = 0
strHeadOrTail = ""

for cnt in range(1,5001):
	strHeadOrTail = "Tail"
	cntTails += 1
	if TossCoin():
		strHeadOrTail = "Head"
		cntHeads += 1
		cntTails -= 1
	print output.format(cnt, strHeadOrTail, cntHeads, cntTails)

