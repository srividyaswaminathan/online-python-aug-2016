def oddEven():
	for x in xrange(1,2001):
		if x % 2 == 0:
			print "The number is " + str(x) + ".  This is an even number."
		else:
			print "The number is " + str(x) + ".  This is an odd number."

oddEven()