## The try - except loop considers exceptions that might arise from your code not running as required and therefore provides way to continue with the code after failure

heystr = "Hello George"
try:
    #try converting the string to a number
    iheystr = int(heystr)
except:
    iheystr = -1

    print("First", iheystr)

    heystr = '123'
    try:
        iheystr = int(heystr)
    except:
        iheystr = -1

    print("Second", iheystr)