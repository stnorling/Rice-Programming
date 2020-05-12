# Examples of mouse input

import simplegui
import math

# intialize globals
width = 450
height = 300
ball_list = []
ball_radius = 15
ball_color = "Red"

# helper function
def distance(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

# define event handler for mouse click, draw

# in the below, without assigning each ball (b) it's own colour in 
# a list, it is difficult to change the cover of given balls individually.
# the below changes all ball colours to green when the distance between
# the mouse click and the existing ball is < ball_radius.
def click(pos):
    global ball_color
    for b in ball_list:
        if distance([b[0], b[1]], [pos[0], pos[1]]) < ball_radius:
            # print b[0], b[1], pos    # Debug 
            ball_color = "Green"
            # break in loop ensures the colour for all balls stays green
            # once the contition is satisfied.
            break
        else:
            ball_color = "Red"
    ball_list.append(pos)

def draw(canvas):
    for b in ball_list:
        canvas.draw_circle(b, ball_radius, 1, "Black", ball_color)
    
# create frame
frame = simplegui.create_frame("Mouse selection", width, height)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()
    