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
def click(pos):
    # when removing elements from a list, we cannot simply use the .remove method
    # on that list as we iterate through it. the total number of iterations cannot
    # decrease during the iteration process.
    
    # instead, we need to create a new list, appropriately named 'remove', which
    # is a list containing all of the elements we wish to remove. We append
    # entries to this list whenever our mouse click position lies within the radius
    # of an existing ball.
    remove = []
    for ball in ball_list:
        if distance(ball, pos) < ball_radius:
            # when the criteria to remove a ball is met, rather than appending
            # the mouse position coordinates (which will likely differ to the 
            # ball coordinates), we append the existing ball, who's radius lies
            # within our mouse position coordinates. This ensures that when we 
            # remove the ball from our ball list later on, the list.index() 
            # method will correctly find the index of the ball we wish to remove, 
            # and the pop method will function accordingly.
            remove.append(ball)

    if remove == []:
        # below appends the pos to our ball_list as a tuple of mouse coordinates
        # for each element appended.
        ball_list.append(pos)
    else:
        for ball in remove:
            ball_list.pop(ball_list.index(ball))

def draw(canvas):
    for ball in ball_list:
        canvas.draw_circle([ball[0], ball[1]], ball_radius, 1, "Black", ball_color)
    
# create frame
frame = simplegui.create_frame("Mouse selection", width, height)
frame.set_canvas_background("White")

# register event handler
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# start frame
frame.start()
    