def draw_stars(list): 
	new_list = []                     
	for x in list:
		if type(x) == str:	          
			value = len(x);     					
			new_list.append(x[0] * value)
		elif type(x) == int:
			value = x
			new_list.append("*" * value)	  
	print(new_list)

a= ["the","quick","brown","fox","jumps"]
b= [1,2,3,4,5,6,7]

draw_stars(b);