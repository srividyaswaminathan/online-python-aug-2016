"""
Pajama Programmer
Coding Dojo - July 5 Online Flex
10-September-2015
Python > Python OOP > Assignment: Car
"""

class Car(object):
    def __init__(self, price=2000, speed=35, fuel="Full", mileage=15):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        print self.display_all()          
    def display_all(self):
        return "Price: " +str(self.price)+ "\nSpeed: " +str(self.speed)+ "mph\nFuel: " +str(self.fuel)+ "\nMileage: " +str(self.mileage)+ "mpg\nTax: " +str(self.tax)+ "\n"


car1 = Car()
car2 = Car(2000, 5, "Not Full", 105)
car3 = Car(2000, 15, "Kind of Full", 95)
car4 = Car(2000, 25, "Full", 25)
car5 = Car(2000, 45, "Empty", 25)
car6 = Car(20000000, 35, "Empty", 15)
