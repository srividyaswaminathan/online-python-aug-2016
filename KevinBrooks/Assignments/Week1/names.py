def print_names(list_of_dict, show_counts):
	output = "{0}{1}{2}{3}"
	format_values = ["",""]
	cntr = 0
	for litem in list_of_dict:
		cntr += 1
		if show_counts:
			format_values[0] = str(cntr) + " - "
			format_values[1] = " - " + str(len(litem["first_name"]) + len(litem["last_name"]))

		print output.format(format_values[0], litem["first_name"] + " ", litem["last_name"], format_values[1])	


def print_users(users_dict):
	for key, data in users_dict.items():
		print key
		print_names(data, True)	


students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

print "*" * 50
print_names(students, False)
	
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

print "*" * 50
print_users(users)

