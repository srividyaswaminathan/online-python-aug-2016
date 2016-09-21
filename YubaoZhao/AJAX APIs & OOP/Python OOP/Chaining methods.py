class Bike(object):
    def __init__(self, price, max_speed, miles=0):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayinfo(self):
        print "Bike's Price:", self.price
        print "Bike's Maximum Speed:", self.max_speed
        if self.miles < 0:
            self.miles = -self.miles
        print "Bike's Total Miles: %d miles"%self.miles
        return self
    def ride(self):
        print "Riding..."
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing..."
        self.miles -= 5
        return self

bike1 = Bike(200, "25mph")
bike2 = Bike(300, "30mph")
bike3 = Bike(400, "35mph")
bike1.ride().ride().ride().reverse().displayinfo()
bike2.ride().ride().reverse().reverse().displayinfo()
bike3.reverse().reverse().reverse().displayinfo()
