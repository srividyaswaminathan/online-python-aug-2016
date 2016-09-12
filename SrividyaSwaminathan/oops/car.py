"""Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. 
If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%. 
Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), 
call this display_all() method to display information about the car once the attributes have been defined."""

class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if (self.price > 10000):
			self.tax = 0.15
		else:
			self.tax = 0.12
		display_all() #will given an error since display_all() has not been defined yet in this line
			
	def display_all(self):
		print "Price:", self.price
		print "Speed:", self.speed
		print "Fuel:", self.fuel
		print "Mileage:", self.mileage
		print "Tax:", self.tax			


#Tuscon is the first instance of Car class
print "tuscon is the first instance if car class"
tuscon = Car(9000, "80mph", "half", "30mpg")
tuscon.display_all()
print "***********************************************"
#Prius is the first instance of Car class
print "prius is the first instance if car class"
prius = Car(3000, "40mph", "kind of empty", "15mpg")
prius.display_all()
print "***********************************************"
#elantra is the first instance of Car class
print "elantra is the first instance if car class"
elantra = Car(13000, "70mph", "full", "25mpg")
elantra.display_all()
print "***********************************************"
#altima is the first instance of Car class
print "altima is the first instance if car class"
altima = Car(19000, "60mph", "half", "28mpg")
altima.display_all()
print "***********************************************"
#maxima is the first instance of Car class
print " maxima is the first instance if car class"
maxima = Car(10000, "65mph", "empty", "25mpg")
maxima.display_all()
print "***********************************************"
#civic is the first instance of Car class
print "civic is the first instance if car class"
tuscon = Car(11000, "50mph", "kind of full", "30mpg")
tuscon.display_all()
print "***********************************************"

