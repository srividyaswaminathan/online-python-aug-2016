def odd_even():
	for i in range(1, 2000):
		if i % 2 == 0:
			print "Number is %s. This is an Even Number" % i
		elif i % 2 != 0:
			print "Number is %s. This is an Odd Number" % i

odd_even()