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

def names():
	for key, data in users.items():
		print key
		num = 1
		for value in data:
			print str(num) + ' - ' + value['first_name'] + ' ' + value['last_name'] + ' - ' + str(len(value['first_name'])+len(value['last_name']))
			num += 1
			
names()