##################
# Object creation and use
# Mutation with Aliasing

class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def set_x(self, newx):
        self.x = newx
    
    def get_x(self):
        return self.x

    
p = Point1(4, 5)
q = Point1(4, 5)
r = p

# as r points to the same object as p, changing x of object p also 
# changes x for object r.
p.set_x(10)

print p.get_x()
print q.get_x()
print r.get_x()
print '========================================='

##################
# Object shared state
# Mutation of shared state

class Point2:
    def __init__(self, coordinates):
        # objects p and q point to the same coordinates variable below. Thus
        # if the coordinates are changed locally or globally, they will 
        # change for both objects.
        self.coords = coordinates
    
    def set_coord(self, index, value):
        # the below can mutate a global variable if self.coords
        # points to a global mutable variable.
        self.coords[index] = value
    
    def get_coord(self, index):
        return self.coords[index]

coordinates = [4, 5]

p = Point2(coordinates)
q = Point2(coordinates)

r = Point2([4, 5])

p.set_coord(0, 10)

print 'coordinates variable value:', coordinates

# as r as pointing to a different list of coordinates (albeit with
# the same values), when the coordinates are changed, it does not
# affect r's coordinates.
print p.get_coord(0)
print q.get_coord(0)
print r.get_coord(0)
print '========================================='


##################
# Objects not sharing state

class Point3:
    def __init__(self, coordinates):
        # by using the list method below, we create a new list, so
        # that our self.coords parameter is no longer pointing 
        # to the global list, but rather a copy its of own. Thus when the 
        # list is mutated, only the local copy is affecte. The 
        # global list remains unchanged.
        self.coords = list(coordinates)
    
    def set_coord(self, index, value):
        self.coords[index] = value
    
    def get_coord(self, index):
        return self.coords[index]

    
coordinates = [4, 5]
p = Point3(coordinates)
q = Point3(coordinates)
r = Point3([4, 5])

p.set_coord(0, 10)

# as can be seen from our print results, only our p object's coordinates
# were mutated from the set_coord method. q and r's coordinates remain 
# unchanged as they are new copies of the original global list.
print p.get_coord(0)
print q.get_coord(0)
print r.get_coord(0)