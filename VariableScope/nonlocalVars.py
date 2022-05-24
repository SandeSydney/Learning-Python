# nonlocal keyword adds a scope override to the inner scope

# Example with an increment function

## The following code will result to an UnboundLocalError because
## num variable is referenced before it's assigned in the innermost function
# def counter():
#     num = 0
#     def incrementer():
#         num += 1
#         return num
#     return incrementer

# c = counter()
# c()
# c()

## To solve above issue, add nonlocal keyword to the mix,
## it will allow you to assign to variables in an outer scope
## Should only be used in a nested function
def counter():
    num = 0
    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer

c = counter()
print(c())
print(c())
print(c())