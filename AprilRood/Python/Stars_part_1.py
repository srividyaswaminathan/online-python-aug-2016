x = [4,6,1,3,5,7,25]

def draw_stars(total):
	for num in range(1,total+1):
		print "*",
	print "\r"

count = 0
for item in x:
	draw_stars(x[count])
	count = count + 1

