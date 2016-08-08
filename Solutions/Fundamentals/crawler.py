# import the urlopen function from the urllib2 module
from urllib2 import urlopen
# import the BeautifulSoup function from the bs4 module
from bs4 import BeautifulSoup
# import pprint to print things out in a pretty way
import pprint
# Construct a PrettyPrinter instance
pp = pprint.PrettyPrinter()
# choose the url to crawl
url = 'http://www.codingdojo.com'
# get the result back with the BeautifulSoup crawler

# Crawl through the site you picked and have your program find all the links on that page. Then go through the results. Create a list of all the unique href locations, and then print the list. Your output should look similar to this:
def print_links(url):
    soup = BeautifulSoup(urlopen(url), 'html.parser')
    links = soup.findAll('a', href=True)
    list_of_links = []
    for link in links:
        if link not in list_of_links:
            list_of_links.append(str(link['href']))
    pp.pprint(list_of_links)

print_links(url)

# Modify your crawler and have it create a dictionary that finds all the links on the page that you crawled. Have each key in your dictionary be the href of the links found. Each key should be unique, meaning that if the same href appeared more than once you increment the count by one.

def print_all_links(url):
    soup = BeautifulSoup(urlopen(url), 'html.parser')
    links = soup.findAll('a', href=True)
    dict_of_links = {}
    for link in links:
        if str(link['href']) in dict_of_links:
            dict_of_links[str(link['href'])] +=1
        else:
            dict_of_links[str(link['href'])] = 1
    pp.pprint(dict_of_links)

print_all_links(url)
