## This script uses the beautiful soup for web scrapping to find the anchor tags ina website

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter Url - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

## get to retrieve all of the anchor tags from the inputted website
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))