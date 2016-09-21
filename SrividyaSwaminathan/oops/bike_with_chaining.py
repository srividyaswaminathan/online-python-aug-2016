"""Create a new class called  Bike with the following properties/attributes:   price, max_speed, miles. Create 3 instances of the Bike class.
Use the __init__() function to specify the price and max_speed of each instance (e.g. bike1 = Bike(200, "25mph"); In the __init__() also write the code so that the initial miles is set to be 0 whenever a
new instance is created. Add the following functions to this class:
displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...
Have the first instance ride three times, reverse once and have it displayInfo(). Have the second instance ride twice, reverse twice and have it displayInfo(). Have the third instance reverse three times and displayInfo().
What would you do to prevent the instance from having negative miles? """

class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def displayInfo(self):
		print "Price of this bike is", self.price	
		print "Maximum speed of this bike is", self.max_speed	
		print "Total miles of this bike is", self.miles

	def ride(self):
		print "Riding" 
		self.miles += 10
		print "Total miles of this bike is", self.miles
		return self

	def reverse(self):
		print "reversing"
		if (self.miles > 0):
			self.miles -= 5
		print "Total miles of this bike is", self.miles
		return self

#Unicorn is the first instance of the bike
unicorn = Bike("$10000", "80mph")
unicorn.ride().ride().ride().reverse().displayInfo()
print "******************************************"
#Pulsar is the second instance of the bike
pulsar = Bike("$5000", "100mph")
pulsar.ride().ride().reverse().reverse().displayInfo()
print "******************************************"
#tvs excel is the third instance of the bike
tvs_excel = Bike("$3000", "40mph")
tvs_excel.reverse().reverse().reverse()