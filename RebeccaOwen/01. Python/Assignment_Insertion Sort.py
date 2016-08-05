# Pajama Programmer
# Coding Dojo - July 5 Online Flex
# 5-August-2016
# Assignment: Insertion Sort

from random import random
from datetime import datetime

def insertion_sort(array):
    #start at index #1
    #if index#1 < index#0
    # copy index#1
    # shift index#0 to #1
    # insert copy into index#1
    # increment index and repeat

    for i in range (1, len(array)):
        while array[i] < array[i-1]:
            copy = array[i]
            array[i] = array[i-1]
            array[i-1] = copy
            if i > 1:
                i-=1
    return array


def create_random_array(n=100, m=10000):
    array = []
    for i in range (n):
        array.append(int(random()*m))
    return array


array = create_random_array()
start = datetime.now()
print insertion_sort(array)
end = datetime.now()
delta = end - start
print '\nTime to sort the array:', delta.total_seconds(), '\n'


