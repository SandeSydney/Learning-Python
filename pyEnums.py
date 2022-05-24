#Enums let you define a fixed number of constant values for a special type of class

from enum import Enum

class Color(Enum):
    red = 1
    green = 2
    blue = 3

#Print out the constants in the Enum
print(Color.red)
print(Color(1))
print(Color['red'])

#Enums are iteratable
print([c for c in Color])