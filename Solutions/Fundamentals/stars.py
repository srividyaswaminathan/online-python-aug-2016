# Create a function called  draw_stars() that takes a list of numbers and prints out  *.

def draw_stars(num_list):
    for string in map(lambda num: insert_stars(num), num_list):
        print string

def insert_stars(num):
    output = ''
    for val in range(0, num):
        output += '*'
    return output

# draw_stars([1,2,7,17,4,12])

# Modify the function above. Allow a list containing integers and strings to be passed to the draw_stars() function. When a string is passed, instead of  displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.

def draw_chars(item_list):
    for string in map(lambda item: insert_chars(item), item_list):
        print string

def insert_chars(item):
    if type(item) == int:
        return insert_stars(item)
    else:
        output = ''
        for val in range(0, len(item)):
            output += item[0]
    return output.lower()

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_chars(x)
