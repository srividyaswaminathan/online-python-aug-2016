#Names
#Part 1, given the following list: 

students = [ 
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def print_names1(arr):
	for value in arr:
		print value['first_name'] + ' ' + value['last_name']

print_names1(students)


#Part 2, given the following dictionary
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

def print_names2(dictionary):
	for key, data in dictionary.items(): 
		val = 1
		print key
		for value in data:
				print str(val) + ' - ' + value['first_name'].upper() + ' ' + value['last_name'].upper() + ' - ' + str(len(str(value['first_name'] + value['last_name'])))
				val += 1

print_names2(users)
