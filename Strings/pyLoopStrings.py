## Looping thru strings using for and while loops

str = 'sugarcane'

## for loop
for letter in str:
    print(letter)

print('\n')

## While loop
idx = 0
while idx < len(str):
    letter = str[idx]
    print(idx, letter)
    idx += 1