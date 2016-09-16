class MathDojo(object):

	def __init__(self):
		self.result = 0

	def add(self, *vals):
		for val in vals:
			if type(val) is list:
				for num in val:
					self.result += num
			else:
				self.result += val
		return self

	def subtract(self, *vals):
		for val in vals:
			if type(val) is list:
				for num in val:
					self.result -= num
			else:
				self.result -= val
		return self		


print (MathDojo().add(2).add(2, 5).subtract(3, 2).result)

print (MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result)