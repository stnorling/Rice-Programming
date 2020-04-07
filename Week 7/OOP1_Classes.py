# A new Class can be thought of as a type. As string, lists, dictionaries are types.. etc.

class Character:
    # self is the instance of given class. You will assign it to a variable name. 
    # think of self as a reference to the new instance of the object.
    
    # __init__ contains arguments self, and as many other arguments as well.
    # the __init__ function, while it doesn't return anything, actually returns the new object
    # that was created.
    def __init__(self, name, initial_health):
        # Below are fields initialized upon creation of the type. 
        # (Data encapsulated inside the type).
        self.name = name
        self.health = initial_health
        self.inventory = []
     
    # __str__ only takes the argument self. 
    def __str__(self):
        s  = "Name: " + self.name
        s += " Health: " + str(self.health)
        s += " Inventory: " + str(self.inventory)
        return s
    
    # Note: You never need to call __init__ or __str__ yourself. Python calls it 
    # automatically itself. You can however call str if you wish. This is done by calling
    # str() of an object that is of the Class type, e.g. str(Character). This calls the
    # __str__ method, and it passes the actual object as self. What is returned is 
    # whatever you defined in the __str__ method. In this case, a print-out of the
    # infromation about the character, returned as a string. 
    
    # Below we define methods that define the behaviors that you can perform
    # on objects of the type. They must take in argument self, and can take in 
    # other arguments of your chosing. 
    def grab(self, item):
        self.inventory.append(item)
        
    def get_health(self):
        return self.health
    
'''
One of the beauties of object oriented programming is that you can define this class 
without worrying about how other people are going to use it. The only way 
that they can use it is by calling these methods that you've created, so you've defined an
interface. And you know that others will obey the interface, so you don't have to worry about
it. You know that someone else is not going to sneak in and decrement your health by 100 behind your
back. You've given others no way to decrease the health of this character, therefore
your health will always be at initial health. If you want to allow others to manipulate the health of
the character you add methods that do so. 

Now you don't have to know anything about how others use it, you know that they'll use it the way
that you intended it.
'''

# Think of creating a class and defining methods of that class as creating an interface that
# can be implemented by you as you build the class, and used by others when they use the class.

def example():
    # Below is how you create an object of your new type. The class name 'Character' becomes the 
    # constructor. 
    me = Character("Bob", 20)
    print str(me)
    me.grab("pencil")
    me.grab("paper")
    print str(me)
    print "Health:", me.get_health()
    
example()
