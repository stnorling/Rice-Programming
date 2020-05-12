# Basic infrastructure for Bubble Shooter

import simplegui
import random
import math

# Global constants
WIDTH = 800
HEIGHT = 600
FIRING_POSITION = [WIDTH // 2, HEIGHT]
FIRING_LINE_LENGTH = 60
FIRING_ANGLE_VEL_INC = 0.02
BUBBLE_RADIUS = 20
COLOR_LIST = ["Red", "Green", "Blue", "White"]

# global variables
firing_angle = math.pi / 2
firing_angle_vel = 0
bubble_stuck = True
inputs = {'left': FIRING_ANGLE_VEL_INC,
          'right': - FIRING_ANGLE_VEL_INC
          }

# firing sound
firing_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/Collision8-Bit.ogg")


# new game

def new_game():
    global a_bubble
    
    a_bubble = Bubble()
    

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0]-q[0])**2+(p[1]-q[1])**2)


# class defintion for Bubbles
class Bubble:
    
    def __init__(self):
        # we make below a list so as to create copies
        self.pos = list(FIRING_POSITION)
        self.vel = [0, 0]
        self.color = random.choice(COLOR_LIST)
        self.sound = firing_sound
    
    def update(self):
        self.pos[1] += self.vel[1]
        if BUBBLE_RADIUS < self.pos[0] + self.vel[0] < WIDTH - BUBBLE_RADIUS:
            self.pos[0] += self.vel[0]
        else:
            self.vel[0] = - self.vel[0]
            self.sound.rewind()
            self.sound.play()
        
        # Below respawns the bubble when it reaches the end
        if self.pos[1] < 0:
            new_game()
        
    def fire_bubble(self, vel):
        self.vel = vel
        self.sound.rewind()
        self.sound.play()
                
    def is_stuck(self): 
        pass

    def collide(self, bubble):
        pass
            
    def draw(self, canvas):
        canvas.draw_circle(self.pos, BUBBLE_RADIUS, 1, 'White', self.color)
        

# define keyhandlers to control firing_angle
def keydown(key):
    global a_bubble, firing_angle_vel, bubble_stuck
    
    for i in inputs:
        if key == simplegui.KEY_MAP[i]:
            firing_angle_vel += inputs[i]
    
    if key == simplegui.KEY_MAP['space']:
        vel = angle_to_vector(firing_angle)
        a_bubble.fire_bubble([vel[0] * 4, vel[1] * - 4])

        
def keyup(key):
    global firing_angle_vel
    
    for i in inputs:
        if key == simplegui.KEY_MAP[i]:
            firing_angle_vel -= inputs[i]
    
    
# define draw handler
def draw(canvas):
    global firing_angle, a_bubble, bubble_stuck
    
    # print statements for debugging show how the angle is converted in to a vector
    # and what the resulting vector x, y coordinates are for a given angle
    
    # update firing angle
    firing_angle += firing_angle_vel
    # print firing_angle
    
    #draw firing line
    orient = angle_to_vector(firing_angle)
    # print orient
    upper_endpoint = [FIRING_POSITION[0] + FIRING_LINE_LENGTH * orient[0], 
                      FIRING_POSITION[1] - FIRING_LINE_LENGTH * orient[1]]
    canvas.draw_line(FIRING_POSITION, upper_endpoint, 4, "White")
    
    # update a_bubble and check for sticking
    
    a_bubble.update()
    
    # draw a bubble and stuck bubbles
    
    a_bubble.draw(canvas)
 
# create frame and register handlers
frame = simplegui.create_frame("Bubble Shooter", WIDTH, HEIGHT)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

# create initial buble and start frame
frame.start()
new_game()