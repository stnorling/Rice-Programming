# Polyline drawing problem

###################################################
# Student should enter code below

import simplegui
import math

polyline = []


# define mouseclick handler
def click(pos):
    polyline.append(pos)
          
# button to clear canvas
def clear():
    polyline = []
    print polyline
    

# define draw
def draw(canvas):
    if len(polyline) > 1:
        canvas.draw_polygon(polyline, 12, "White")
    elif len(polyline) == 1:
        canvas.draw_point(polyline[0], "White")
        
                   
# create frame and register handlers
frame = simplegui.create_frame("Echo click", 300, 200)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)
frame.add_button("Clear", clear)

# start frame
frame.start()

