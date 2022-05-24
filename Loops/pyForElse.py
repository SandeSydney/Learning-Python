## For...Else... strange but some loops condition remains true as long as the iterable object or sequence still has remaining elements

## For...Else.. used in python to implement search

a = [1,2,3,4,5]

for i in a:
    if type(i) is not int:
        print(i)
        break

else: 
    print("No exception!")

## Pass keyword in python serves as a placeholder. Nothing is intended to be done at that moment
# Allows code to run successfully without having all commands and actions fully implemented

for x in range(10):
    pass # Nothing is implemented. Can be used in the future