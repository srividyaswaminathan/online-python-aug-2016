x = [4, 6, 1, 3, 5, 7, 25]

def draw_stars(x):
	for i in xrange(0,len(x)):
		y = 0
		while y<x[i]:
			print "*",
			y += 1
		print ""


draw_stars(x)