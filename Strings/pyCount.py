## Program to count the number of letter 'a' in the word supplied

word = 'alphabetically'
count = 0   # set the initial count to 0
for letter in word:
    if letter == 'a':
        count += 1

print(count)