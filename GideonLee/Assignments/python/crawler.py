# import the urlopen function from the urllib2 module
from urllib2 import urlopen
from bs4 import BeautifulSoup
# choose the url to crawl
url = 'http://www.codingdojo.com'

def find_all_unique_links(url):
	locations = []
	unique_locations = []
	soup = BeautifulSoup(urlopen(url), 'html.parser')
	# find all links to locations
	for link in soup.find_all('a'):
		locations.append(link.get('href'))
	# push all unique links to unique_locations
	for link in locations:
		if link not in unique_locations:
			unique_locations.append(link)
	# print all the unique links
	for link in unique_locations:
		print link
	return unique_locations

find_all_unique_links(url)

print '*' * 50

def dict_of_links(url):
	locations = []
	soup = BeautifulSoup(urlopen(url), 'html.parser')
	for link in soup.find_all('a'):
		locations.append(link.get('href'))

	href_dict = {}
	for link in locations:
		if href_dict.has_key(link):
			href_dict[link] += 1
		else: 
			href_dict[link] = 1
	for link, data in href_dict.items():
		print link, '-', data
	return href_dict	

dict_of_links(url)