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

def print_lib(lib):
	for x in lib:
		print x
		for i, person in enumerate(lib[x]):
			print "{} - {} {} - {}".format(i+1, person['first_name'].upper(),person['last_name'].upper(),len(person['first_name'])+len(person['last_name']))

print_lib(users)


