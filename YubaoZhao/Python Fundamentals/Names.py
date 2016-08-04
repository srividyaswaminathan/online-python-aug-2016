#Assignment: Names

#Part I
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def print_student_fullname(dict):
    for name in dict:
        print name['first_name'],name['last_name']
print_student_fullname(students)

#Part II
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
def print_user_fullname(dict):
    for user,data in dict.items():
        print user
        idx = 1
        for name in data:
            fir = name['first_name'].upper()
            las = name['last_name'].upper()
            print "{} - {} {} - {}".format(str(idx),fir,las,len(fir+las))
            idx += 1
print_user_fullname(users)
