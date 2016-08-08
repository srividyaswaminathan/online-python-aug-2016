#Assignment: Bubble Sort

#Populate a sample list with 100 values (where each value is a random number between 0 to 10000).
#Implement a bubble sort algorithm that returns a new list that's sorted (with smallest number on the left).
#Do this without creating another list.

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

def bubble_sort(list):
    count = 0
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            count += 1
            if list[j] > list[j+1]:
                list[j+1],list[j] = list[j],list[j+1]
    return (list,count)

list = generate_list()
print "========================"
print "Original list:",list
print
print "  Sorted list:",bubble_sort(list)[0]
print
print "If/else Statements Counter:",bubble_sort(list)[1]
