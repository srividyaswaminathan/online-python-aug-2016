#Assignment: Stars

#Part 1
#Create a function called  draw_stars() that takes a list of numbers and prints out *.

def draw_stars(arr):
    for num in arr:
        star = ""
        for i in range(num):
            star += "*"
        print star

x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)

#Part 2
#Modify the function above. Allow a list containing integers and strings to be
#passed to the  draw_stars() function. When a string is passed, instead of
#displaying *, display the first letter of the string according to the example
#below. You may use the .lower() string method for this part.

def draw_stars2(arr):
    for item in x:
        if type(item) == int:
            star = ""
            for i in range(item):
                star += "*"
            print star
        elif type(item) == str:
            letter = ""
            for i in range(len(item)):
                letter += item[0].lower()
            print letter

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars2(x)
