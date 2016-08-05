import re
from urllib2 import urlopen
from bs4 import BeautifulSoup
import pprint
url = 'http://www.codingdojo.com'
soup = BeautifulSoup(urlopen(url), "html.parser")
# print soup
hrefs = re.findall(r'href="([^" >]+)', str(soup))
links = {}
for href in hrefs:
	if href in links:
		links[href] += 1
	else:
		links[href] = 1
print links

# had problems getting the dictionary to print nicer. Keys would be fine, but values would be missing.