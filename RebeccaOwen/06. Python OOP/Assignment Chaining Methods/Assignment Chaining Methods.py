"""
Pajama Programmer
Coding Dojo - July 5 Online Flex
10-September-2015
Python > Python OOP > Assignment Chaining Methods
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
        print ""
        return self
    def ride(self):
        print "Just riding along..."
        self.miles += 10
        return self
    def reverse(self):
        if ((self.miles - 5) >= 0):
            print "beep beep, going backwards!"
            self.miles -= 5
        else:
            print "I will not move backwards!"
        return self

bike1 = Bike()
bike1.ride().ride().ride().reverse().displayInfo()

bike2 = Bike(200, 50)
bike2.ride().ride().reverse().reverse().displayInfo()

bike3 = Bike(45, 3)
bike3.reverse().reverse().reverse().displayInfo()
