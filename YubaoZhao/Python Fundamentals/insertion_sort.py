#Assignment: Insertion Sort

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

def insertion_sort(list):
    import datetime
    count = 0
    begin_time = datetime.datetime.now()
    for i in range(1,len(list)):
        for j in range(i-1,-1,-1):
            count += 1
            if list[i] < list[j]:
                list[i],list[j] = list[j],list[i]
                i -= 1
    end_time = datetime.datetime.now()
    time = end_time - begin_time
    return (list,count,time)

list = generate_list()
print "========================"
print "Original List:",list
print
print "  Sorted List:",insertion_sort(list)[0]
print
print "If/else Statements Counter:",insertion_sort(list)[1]
print
print "Time Counter: {}s".format(insertion_sort(list)[2])
