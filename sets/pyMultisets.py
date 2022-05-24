# In order to implement multisets, we are provided with the Counter Class from the Collections module
# Reason is that we sometimes want to keep the duplicates in a set. 

from collections import Counter
counterA = Counter(['a','b','b','c'])
print(counterA)