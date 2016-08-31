x = [4,"Tom",1,"Michael",5,7,"Jimmy Smith"]

def draw_stars(cycles, symbol):
	for num in range(1,cycles+1):
		print symbol,
	print "\r"

count = 0
for item in x:
	if type(item) is int:
		draw_stars(x[count],"*")
	else:
		chkStr = x[count]
		draw_stars(len(chkStr),chkStr[:1].lower())
	
	count = count + 1

