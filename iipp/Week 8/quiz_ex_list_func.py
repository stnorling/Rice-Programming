class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def translate(self, deltax=0, deltay=0):
        """Translate the point in the x direction by deltas 
           and in the y direction by deltay."""
        self.x += deltax
        self.y += deltay

    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"
    
point = Point2D(3, 6)
# when using the list() function, the argument must be an iterable
lst = list(point)
