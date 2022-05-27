## Python script to read files. 
## done by creating a file handler and reading from it

fhand1 = open('sample1.txt')

# Iterate over the file to display text
for text in fhand1:
    print(text)

# 2nd file handler
fhand2 = open('sample2.txt')
for text in fhand2:
    print(text)