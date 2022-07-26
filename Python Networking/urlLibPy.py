## This script uses the python library urllib to connect to the internet and get stuff for us. 
## Automatically encodes, sends and retrieves data for us. 
## We're only required to decode and loop through a fileHandler structure

import urllib.request, urllib.parse, urllib.error

# pass in the website you want to get data from
flHand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# dictionary to count words in the website
counts = dict()
for line in flHand:
    wrds = line.decode().split()
    for wrd in wrds:
        counts[wrd] = counts.get(wrd, 0) + 1
print(counts)