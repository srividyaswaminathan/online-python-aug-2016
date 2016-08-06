students = [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for student in students:
	print student['first_name'] + " " + student['last_name'] 

print "*******************************************************"
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



for key, values in users.iteritems():
	print key
	i = 1
	for value in values:
		name = value["first_name"] + " " + value["last_name"] 
		len_name = len(name) - name.count(' ') #to avoid counting on spaces
		print str(i)+" " + name + "-" + str(len_name)
		i = i +1


