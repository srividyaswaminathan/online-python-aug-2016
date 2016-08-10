def draw_stars(arr):
	for value in arr:
		char = "*"
		cnt = 0
		if isinstance(value, int):
			cnt = int(value)
		else:
			char = value[0].lower()
			cnt = len(value)

		print (char * cnt)

print "-- INT ARRAY --"

x = [4,6,1,3,5,7,25]

draw_stars(x)

print "-- MIXED ARRAY --"

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars(x)