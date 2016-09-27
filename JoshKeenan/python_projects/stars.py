def draw_stars(list): 
	new_list = []                     
	for x in list:
		if type(x) == str:	          
			value = len(x);     					
			print(x[0] * value)
		elif type(x) == int:
			value = x
			print("*" * value)	  
	# print(new_list)

a= ["the","quick",8,"fox",12]
b= [1,2,3,4,12,6,7]

draw_stars(a)