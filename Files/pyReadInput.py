## Script to read a file from the system after user has specified the file
## Has a fail-safe mechanism

fname = input('Type file name: ')
try:
    fhand = open(fname + '.txt')
except:
    print('Not a valid file! :' , fname)
    quit()
for line in fhand:
    print(line.strip())