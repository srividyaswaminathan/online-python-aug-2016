class Underscore(object):
    def map(self, list, callback):
        for i in range(len(list)):
            list[i] = callback(list[i])
        return list
        
    def reduce(self, list, callback):
        i = 1
        num = list[0]
        for i in range(len(list)):
            num = callback(num, list[i])
        return num

    def find(self, list, callback):
        new_list = []
        for val in list:
            if callback(val):
                new_list.append(val)
        return new_list

    def filter(self, list, callback):
        return_list = []
        for val in list:
            if callback(val):
                return_list.append(val)
        return return_list

    def reject(self, list, callback):
        return_list = []
        for val in list:
            if not callback(val):
                return_list.append(val)
        return return_list

_ = Underscore() 
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print ('evens:', evens)

maps = _.map([1, 2, 3, 4, 5, 6], lambda x: x ** 2)
print ('map:', maps)

num = _.reduce([1,2,3,4], lambda x,y : x + y)
print ('reduce:', num)

filtered = _.filter([1,2,3,4,5,6,7,8,9], lambda x: x > 4)
print ('filter:', filtered)

rejected = _.reject([1,2,3,4,5,6,7,8,9], lambda x: x > 4)
print ('reject:', rejected)