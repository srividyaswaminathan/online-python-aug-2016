# Optional Assignment: Radix Sort
from random import randint
from datetime import datetime

def random_list():
    list = []
    while 1:
        len = input("Input List Length:")
        if len > 1:
            break
        else:
            print "Invalid Value!"
            continue
    for i in range(len):
        list.append(randint(0,9999))
    return list

def get_digit_from_position(num,pos):
    digit = (num / 10**pos) % 10
    return digit

def generate_list(two_dimension_list):
    list =[]
    for row in two_dimension_list:
        for num in row:
            list.append(num)
    return list

def radix_sort(list):
    begin_time = datetime.now()
    for i in range(4):            # number in the random list is from 0--9999,there are 4 digits
        two_dim_list = [[] for j in range(10)]   # create a two-dimensin list
        for num in list:
            digit = get_digit_from_position(num,i)
            two_dim_list[digit].append(num)
        list = generate_list(two_dim_list)
    end_time = datetime.now()
    time = end_time - begin_time
    return (list,time)


list = random_list()
print "========================"
print "Original List:",list
print
print "  Sorted List:",radix_sort(list)[0]
print
print "Operations Counter:{}".format(4*len(list))  # digits * numbers of list
print
print "Time Counter: {}s".format(radix_sort(list)[1])
