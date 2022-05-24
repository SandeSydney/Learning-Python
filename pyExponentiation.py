# Making exponents of numbers

a,b = 2,3

# Method 1 of exponentiation
exp1 = (a ** b)

# Method 2 using pow()
exp2 = pow(a, b)

# Method 3 using pow() from math Builtin
import math
exp3 = math.pow(a, b) # Always returns floats; does not allow complex results

# Method 4 using pow() from operator builtin
import operator
exp4 = operator.pow(a, b)

print(exp1)
print(exp2)
print(exp3)
print(exp4)

print("\n")

# Finding other roots of a number, Raise the number to the reciprocal of the degree of the root

# eg cuberoot of 8
x = 8
cbrt = math.pow(8, 1/3)
print(cbrt)

# example 2
y = 64
rt = math.pow(16, 1/4)
print(rt)