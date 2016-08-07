import re
from urllib2 import urlopen
from bs4 import BeautifulSoup
import pprint
url = 'http://www.codingdojo.com'
soup = BeautifulSoup(urlopen(url), "html.parser")
# print soup
hrefs = re.findall(r'href="([^" >]+)', str(soup))
links = []
for href in hrefs:
	links.append(href)
print '\n'.join(links)