# Pajama Programmer
# Coding Dojo - July 5 Online Flex
# 3-August-2016
# Assignment: Names

# Part I

##Given the following list:

students = [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

##Create a program that outputs:

##Michael Jordan
##John Rosales
##Mark Guillen
##KB Tonel

for student in students:
    print student['first_name'], student['last_name']

print ''

##Part II
##
##Now, given the following dictionary:

users = {
    'Students': [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
##Create a program that prints  the following format (including number of characters in each combined name):
##
##Students
##1 - MICHAEL JORDAN - 13
##2 - JOHN ROSALES - 11
##3 - MARK GUILLEN - 11
##4 - KB TONEL - 7
##Instructors
##1 - MICHAEL CHOI - 11
##2 - MARTIN PURYEAR - 13

for user in users:
    count = 1
    print user
    for name in users[user]:
        total = len(name['first_name']) + len(name['last_name'])
        print count, '-', name['first_name'], name['last_name'], '-', total
        count += 1
