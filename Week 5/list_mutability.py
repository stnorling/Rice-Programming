# as can be seen below, lists are mutable per element,
# but when reassigning the whole list, as in function2, 
# the variable must be declared global, otherwise it only
# creates the list locally and the global list remains
# unchanged.

point = [0, 0]

def function1():
    point[0] += 1
    point[1] += 2

function1()
print point

def function2():
    global point
    point = [50, 50]

function2()
print point