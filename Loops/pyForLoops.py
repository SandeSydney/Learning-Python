## For lopps iterate over a collection such as Lists and Dicts
## They run the block of code with each element from the iteration

# Iterate over a list of numbers
for i in [0,1,2,3,4,5]:
    print(i)

print("\n")

# range returns a series of numbers under an iterable form, therefore can be used in for loops
for i in range(5):
    print(i)

print("\n")

# Range generates a bunch of numbers that can be used in a for loop
for x in range(1, 6):
    print(x)

print("\n")

## Iterating over Lists
for x in ["One", "Two", "Three", "Four"]:
    print(x)

## To loop through both elements of a list, an index and the item, you can use python's enumerate function
for index, item in enumerate(["one", "two", "three", "four"]):
    print(index, "::", item)

print("\n")

## One can iterate over a list with manipulating values using 'map' and 'lambda'
x = map(lambda e: e.upper(), ['one', 'two', 'three', 'four'])
print(list(x)) # In python 3 use print(list(x)), in python 2 use print(x)