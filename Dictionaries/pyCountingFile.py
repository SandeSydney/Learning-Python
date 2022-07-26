## Program to count number of words read froma file and output their histogram.

# Empty dictionaty
word_grp = dict()

# Read from file
fname = input('Type the file to read from: ')
fhandle = open(fname)

# iterate over file handle, split words and count them 
for line in fhandle:
    words = line.split()
    for word in words:
        word_grp[word] = word_grp.get(word, 0) + 1

## find the word with the largest count in the word_grp
large_count = None
large_word = None
for word,count in word_grp.items():
    if large_count is None or count>large_count:
        large_word = word
        large_count = count

print(large_word, large_count)