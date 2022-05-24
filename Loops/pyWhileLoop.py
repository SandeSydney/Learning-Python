## While loops function to provide iteration
## break keyword stops the iteration
## Iterate must be used in order to control number of times a loop runs. 

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Done!')