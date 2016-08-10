from urllib2 import urlopen
from bs4 import BeautifulSoup
import pprint

url = "http://www.codingdojo.com"
soup = BeautifulSoup(urlopen(url), "html.parser")
#print soup
links = soup.findAll('a', href= True)
list_links = []
dict_links = {}
count = 0
for link in links:
	individual_link = link['href']
	if individual_link not in list_links:
		count =  1
	else:
		count = dict_links[individual_link] + 1
	
	list_links.append(individual_link)
	dict_links[individual_link] = count

for link, count in dict_links.iteritems():
	print link + "=" + str(count)		



