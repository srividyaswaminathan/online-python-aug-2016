#Average List
# Create a program that prints the average of the values in the list:
# a = [1, 2, 5, 10, 255, 3]

a = [1,2,5,10,255,3]

def average_list(arr):
    sum = arr[0]
    for num in arr[1:]:
        sum += num
    return sum / len(arr)

print "Average is:",average_list(a)
