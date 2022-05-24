## Functions skip class scope when looking up names

a = "global"


## In definition, class has a local scope
## functions inside the class do not use that scope when looking up names
class Sande:
    a = "Class"                 # Class scope
    b = (a for i in range(10))  # function scope
    c = [a for i in range(10)]  # function scope
    d = a                       # class scope
    e = lambda: a               # function scope
    f = lambda a=a: a           # default argument uses class scope

    @staticmethod   # or @classmethod, or regular instance method
    def g():        # function scope
        return a

# Print statements to display the results
print(Sande.a)
print(next(Sande.b))
print(Sande.c[0])
print(Sande.d)
print(Sande.e())
print(Sande.f())
print(Sande.g())