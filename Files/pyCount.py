## Script to count the number of lines from a file read

fhand = open('sample3.txt')
count = 0
for line in fhand:
    count += 1
print('Number of lines = ', count)