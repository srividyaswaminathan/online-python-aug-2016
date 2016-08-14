# import the urlopen function from the urllib2 module
from urllib2 import urlopen
# import the BeautifulSoup function from the bs4 module
from bs4 import BeautifulSoup
# import pprint to print things out in a pretty way
import pprint
# choose the url to crawl
url = 'http://www.codingdojo.com'
# get the result back with the BeautifulSoup crawler
soup = BeautifulSoup(urlopen(url))
#print soup # print soup to see the result!!
# your code here to find all the links from the result
# and complete the challenges below

links_list = []
links_dictionary = {}

for a in soup.body.findAll("a"):
	links_list.append(a["href"])

for item in links_list:
	if (links_dictionary.has_key(item)):
		links_dictionary[item] = int(links_dictionary[item]) + 1
	else:
		links_dictionary[item] = 1

for key, value in links_dictionary.iteritems():
	print key + ":" + str(value)
