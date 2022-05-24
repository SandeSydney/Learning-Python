## Any assignment inside a scope will shadow any outer variables of the same name

## By declaring a name global means that any assignments will happen
## at the modules top level, for the rest of the scope

x = "Hi"

def change_global_x():
    global x
    x = "Bye"
    print(x)

change_global_x()
print(x)