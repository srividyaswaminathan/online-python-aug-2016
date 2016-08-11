import re

x = "This is my test string. Cooooool. Author:Kevin"

match = re.search(r"Author:\w\w\w\w\w", x)

if match:
	print "found the author: " + match.group()
else:
	print "no match"

match = re.search(r"Co+", x)

if match:
	print "found " + match.group() 

email = "some-body@codingdojo.com"

match = re.search(r"([\w.-]+)@([\w.-]+)", email)

if match:
	print match.group()
	print match.group(1)
	print match.group(2)

email = "kb@codingdojo.com, mike@codingdojo.com, joe@codingdojo.com"

match = re.findall(r"([\w.-]+)@([\w.-]+)", email)

for item in match:
	print "@".join(item)