def get_array():
    array = []
    for i in range (1,256):
        array.append(i)
    print array

get_array()

def get_odds():
    array = []
    for i in range (1,256):
        if i%2==1:
            array.append(i)
    print array

get_odds()

def intsandsum():
    array = []
    sum = 0
    for i in range (0,256):
        array.append(i)
        sum += i
        print sum
    print array

intsandsum()

arr = [2,4,12,44]
def vals(values_list):
    for i in range (len(arr)):
        print "array " + str(i) + " is equal to " + str(arr[i])

vals(arr)

#def findMax(arr):
arr = [3,12,5,22,1]

def findMax(arr):
    max = 0
    for i in range (len(arr)):
        if arr[i] > max:
            max = arr[i]
    print max

findMax(arr)

arr = [3,12, 55, 1, 3]
def findAvg(arr):
    sum = 0
    for i in range (len(arr)):
        sum += arr[i]
        avg = sum/len(arr)
    print avg

findAvg(arr)

def returnOdds():
    arr = []
    for i in range (1, 256):
        if i%2==1:
            arr.append(i)
    print arr

returnOdds()


def squareArray():
    for i in range (len(arr)):
        arr[i] = arr[i] * arr[i]
    print arr

squareArray()
