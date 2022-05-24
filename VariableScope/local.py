## If a name is bound inside a function, it's accessible only within the function by default

def loc_func():
    a = 5
    print(a) # This is okay

loc_func()

#  print(a) # This won't work. NameError: name 'a' is not defined