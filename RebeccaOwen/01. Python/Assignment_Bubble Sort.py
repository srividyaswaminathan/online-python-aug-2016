# Pajama Programmer
# Coding Dojo - July 5 Online Flex
# 2-August-2016
# Assignment: Bubble Sort

from random import random
from datetime import datetime

def bubble_sort(array):
    end = len(array)
    while end > 1:
        for i in range (end-1):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
        end -= 1
        #print array    
    return array

def create_random_array(n=100, m=10000):
    array = []
    for i in range (n):
        array.append(int(random()*m))
    return array
    
array = [6,5,3,1,7,2,8,4]
array = [8,7,6,5,4,3,2,1]

array = create_random_array()

start = datetime.now()
print bubble_sort(array)
end = datetime.now()
delta = end - start
print '\nTime to sort the array:', delta.total_seconds()


