#Importing the whole hello module
import hello

print(hello.say_hello())

#Importing specific parts of a module
from hello import say_hello
print(say_hello())

#Using an alias on imported module
import hello as ai 
print(ai.say_hello())