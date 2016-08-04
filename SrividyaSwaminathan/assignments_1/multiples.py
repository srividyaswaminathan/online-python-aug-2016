# printing all odd numbers from 1-1000

def odd_number():
	for x in range(1,1000):
		if(x%2!=0):
			print x


#print all multiples of 5 from 5 to 1,000,000

def mul_of_five():
	for x in range(5, 1000000):
		if x%5 == 0:
			print x

