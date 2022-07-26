## Code to use dictionatries to achieve a histogram by counting number of items in a dictionary

totals = dict()
items = ['simiyu', 'joan', 'wekesa', 'simiyu', 'wekesa', 'natalie', 'joan', 'simiyu', 'kipchumba', 'mohammed', 'kipchumba']

# Iterating over the list and creating new items or adding value onto existing
for item in items:
    totals[item] = totals.get(item, 0) + 1
print(totals)