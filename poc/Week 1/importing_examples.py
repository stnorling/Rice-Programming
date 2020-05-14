# Import the math module (look in the Docs for help)
import math

# Import example module
import examples_module as example

# Constants
print "===Math constants==="

print math.pi
print math.e

# Functions
print
print "===Math functions==="

print math.sqrt(25)
print math.trunc(14.83483)
print math.sin(math.pi / 2.0)

# Dir
print
print "===Dir==="

# the pyton dir function can be used to find all of the properties (or constants), 
# functions and Classes of a module. 

print dir(math)
print dir(example)

print example.message

print math.__name__
print example.__name__


import user47_cGRC7Nv8MeWPzG7_8 as rice_rocks

print dir(rice_rocks)

# below is an example of using the dir function to find all of the 
# methods in a given Class of a module

print dir(rice_rocks.Ship)