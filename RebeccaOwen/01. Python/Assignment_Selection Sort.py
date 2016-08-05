# Pajama Programmer
# Coding Dojo - July 5 Online Flex
# 4-August-2016
# Assignment: Selection Sort

from random import random
from datetime import datetime

def selection_sort(array):
    #min_index - index that smallest value will go to
    for min_index in range (0, len(array)-1):
        min_loc = min_index     #min_loc, smallest value found so far
        for i in range (min_loc, len(array)):
            if array[i] < array[min_loc]:   #Update min_loc
                min_loc = i

        #Swap min_loc/min_index
        temp = array[min_index]
        array[min_index] = array[min_loc]
        array[min_loc] = temp  
    return array

def selection_sort_2(array):
    for min_index in range (0, len(array)/2):
        max_index = len(array)-1-min_index
        min_loc = min_index
        max_loc = max_index
    
        for i in range (min_index, max_index):
            if array[i] < array[min_loc]:
                min_loc = i
            if array[len(array)-i-1] > array[max_loc]:
                max_loc = i

            temp = array[min_index]
            array[min_index] = array[min_loc]
            array[min_loc] = temp
            temp = array[max_index]
            array[max_index] = array[max_loc]
            array[max_loc] = temp
        
    return array

def create_random_array(n=100, m=10000):
    array = []
    for i in range (n):
        array.append(int(random()*m))
    return array


array = create_random_array()
start = datetime.now()
print selection_sort(array)
end = datetime.now()
delta = end - start
print '\nTime to sort the array:', delta.total_seconds(), '\n'

start = datetime.now()
print selection_sort_2(array)
end = datetime.now()
delta = end - start
print '\nTime to sort the array:', delta.total_seconds()


