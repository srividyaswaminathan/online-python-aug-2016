#Assignment: Selection Sort

def generate_list():
    import random
    list = []
    while 1:
        len = input("Input List Length:")
        if len > 1:
            break
        else:
            print "Invalid Value!"
            continue
    for i in range(len):
        list.append(random.randint(0,10000))
    return list

def selection_sort(list):
    import datetime
    count = 0
    begin_time = datetime.datetime.now()
    for i in range(0,len(list)-1):
        min = list[i]
        min_idx = i
        for j in range(i+1,len(list)):
            count += 1
            if min > list[j]:
                min = list[j]
                min_idx = j
        list[i],list[min_idx] = list[min_idx],list[i]  #swap value
    end_time = datetime.datetime.now()
    time = end_time - begin_time
    return (list,count,time)

list = generate_list()
print "========================"
print "Original List:",list
print
print "  Sorted List:",selection_sort(list)[0]
print
print "If/else Statements Counter:",selection_sort(list)[1]
print
print "Time Counter: {}s".format(selection_sort(list)[2])
