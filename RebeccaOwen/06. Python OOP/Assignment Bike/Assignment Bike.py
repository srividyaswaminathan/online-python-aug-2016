"""
Pajama Programmer
Coding Dojo - July 5 Online Flex
10-September-2015
Python > Python OOP > Assignment: Bike
"""

class Bike(object):
    def __init__(self, price=100, speed=25):
        print 'A new bike has been created'
        self.price = price
        self.max_speed = speed
        self.miles = 0
    def displayInfo(self):
        print "Price         : $" + str(self.price)
        print "Maximum Speed : " + str(self.max_speed) + " mph"
        print "Total Miles   : " + str(self.miles)
    def ride(self):
        print "Just riding along..."
        self.miles += 10
    def reverse(self):
        if ((self.miles - 5) >= 0):
            print "beep beep, going backwards!"
            self.miles -= 5
        else:
            print "I will not move backwards!"

bike1 = Bike()
for i in range(3):
    bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike(200, 50)
for i in range(2):
    bike2.ride()
for i in range(2):
    bike2.reverse()
bike2.displayInfo()

bike3 = Bike(45, 3)
for i in range(3):
    bike3.reverse()
bike3.displayInfo()
