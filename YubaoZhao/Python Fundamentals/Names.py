#Assignment: Names

#Part I
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def print_student_fullname(dict):
    for student_dict in dict:
        print student_dict['first_name'],student_dict['last_name']
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
        for idx in range(len(data)):
            fir = data[idx]['first_name'].upper()
            las = data[idx]['last_name'].upper()
            print "{} - {} {} - {}".format(idx+1,fir,las,len(fir+las))
print_user_fullname(users)
