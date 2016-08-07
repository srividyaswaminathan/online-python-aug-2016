x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars(x):
	for i in xrange(0,len(x)):
		val = str(x[i])
		y = 0
		if val.isdigit():
			while y<x[i]:
				print "*",
				y += 1
		else:
		 	z = len(x[i])
		 	while y<z:
		 	 	print x[i][0].lower(),
	 		 	y += 1
		print ""


draw_stars(x)