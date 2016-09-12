class Animal(object):

	def __init__(self):
		self.name = 'animal'
		self.health = 100

	def walk(self):
		self.health -= 1
		return self

	def run(self):
		self.health -= 5
		return self

	def displayHealth(self):
		print (self.name + ' : ' + str(self.health))
		return self

class Dog(Animal):

	def __init__(self):
		super(Dog, self).__init__()
		self.health += 50
		self.name = 'dog'

	def pet(self):
		self.health += 5
		return self

class Dragon(Animal):

	def __init__(self):
		super(Dragon, self).__init__()
		self.health += 70
		self.name = 'dragon'

	def fly(self):
		self.health -= 10
		return self

	def displayHealth(self):
		print 'this is a dragon!'
		super(Dragon, self).displayHealth()
		return self


animal = Animal()
animal.walk().walk().walk().run().run().displayHealth()

dog = Dog()
dog.walk().walk().walk().run().run().pet().displayHealth()

dragon = Dragon()
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()