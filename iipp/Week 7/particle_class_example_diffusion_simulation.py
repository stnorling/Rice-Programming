# Particle class example used to simulate diffusion of molecules

import simplegui
import random

# global constants
WIDTH = 600
HEIGHT = 400
PARTICLE_RADIUS = [5, 3, 8, 1, 4]
COLOR_LIST = ["Red", "Green", "Blue", "White"]
DIRECTION_LIST = [[1,0], [0, 1], [-1, 0], [0, -1]]


# definition of Particle class
class Particle:
    
    # initializer for particles
    def __init__(self, position, color, radius):
        # position argument is in the format [x, y].
        self.position = position
        self.color = color
        self.radius = radius
        
    # method that updates position of a particle    
    def move(self, offset):
        self.position[0] += offset[0]
        self.position[1] += offset[1]
        
    # draw method for particles
    def draw(self, canvas):
        canvas.draw_circle(self.position, self.radius, 1, self.color, self.color)
    
    # string method for particles
    # When we use str() or print on the particle object, the below is printed to the console.
    def __str__(self):
        return "Particle with position = " + str(self.position) + " and color = " + self.color \
                + " and radius = " + str(self.radius)


# draw handler
def draw(canvas):
    for p in particle_list:
        # random.choice(a_seq) Returns a random element from the non-empty sequence a_seq. 
        # If a_seq is empty, raises an IndexError.
        
        # By passing in DIRECTION_LIST as the argument of the move(offset) method for the
        # Particle object, we can see that the Particle's position will update randomly 
        # according to the choice of value in DIRECTION_LIST.
        p.move(random.choice(DIRECTION_LIST))
        p.draw(canvas)


# create frame and register draw handler
frame = simplegui.create_frame("Particle simulator", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# create a list of particles
particle_list = []
for i in range(1000):
    # Each iteration below creates a new unique Particle object. Once appended to the list, they
    # are a value of their own. The fact that the 'p' variable references the same value is 
    # irrelevant. They are all unique entries to the list. Keep in mind, 'p' is overwriting
    # itself per each iteration of the loop.
    p = Particle([WIDTH / 2, HEIGHT / 2], random.choice(COLOR_LIST), random.choice(PARTICLE_RADIUS))
    particle_list.append(p)
    
print particle_list
print particle_list[0]
# start frame
frame.start()
