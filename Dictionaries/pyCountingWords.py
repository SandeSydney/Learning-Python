## Program to count each number of words supplied and stack them in a dictionary

# Empty dictionary
word_grp = dict()

# Take input,strip, and split
sentence = input('Enter sentence of text here: ').strip()
words = sentence.split()

print('Counting the words...')

for word in words:
    word_grp[word] = word_grp.get(word, 0) + 1
print('Word group: ', word_grp)