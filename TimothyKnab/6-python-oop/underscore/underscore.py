############
#
#	_.Underscore Assignment (build a custom method library using lambda functions)
#		Tim Knab - Coding Dojo - September 2016
#
############

class Underscore(object):

	def map(self, myList, function):
		newList = []
		for x in range(len(myList)):
			newList.append(function(myList[x]))
		print newList

	def reduce(self, myList, function):
		value = 0
		for x in range(len(myList)):
			value += function(myList[x])
		print value

	def find(self, myList, function):
		value = 0
		for x in range(len(myList)):
			if function(myList[x]):
				value = myList[x]
				print value
				break

	def filter(self, myList, function):
		newList = []
		for x in range(len(myList)):
			if function(myList[x]):
				newList.append(myList[x])
		print newList

	def reject(self, myList, function):
		newList = []
		for x in range(len(myList)):
			if not function(myList[x]):
				newList.append(myList[x])
		print newList


_ = Underscore()
_.filter([1,2,3,4,5,6], lambda x : x % 2 == 0)
_.map([1,2,3], lambda x : x * 3)
_.reduce([1,2,3], lambda x: x )
_.find([1,2,3,4,5,6], lambda x: x % 2 == 0)
_.reject([1,2,3,4,5,6], lambda x: x % 2 == 0)