
#print a number and priting if its odd or even 

def odd_even():
	for x in range(1,2001):
		if(x%2==0):
			print "Number is", str(x) + "." + " " +"This is an even number" + "."
		else:
			print "Number is", str(x) + "."+ " " +"This is an odd number" + "."

print odd_even()

