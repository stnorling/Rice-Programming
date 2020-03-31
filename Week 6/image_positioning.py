# Image positioning problem

###################################################
# Student should enter code below

import simplegui

# global constants
WIDTH = 400
HEIGHT = 300
asteroid_w = 95
asteroid_h = 93
pos = [WIDTH / 2, HEIGHT / 2]

# load test image
asteroid = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid.png")

# mouseclick handler
def click(mpos):
    global pos
    pos = mpos

# mousedrag handler
def drag(mpos):
    global pos
    if abs(pos[0] - mpos[0]) < (asteroid_w / 2) and abs(pos[1] - mpos[1]) < (asteroid_h / 2):
        # print pos, mpos
        pos = mpos
    
# draw handler
def draw(canvas):
    canvas.draw_image(asteroid,[asteroid_w / 2, asteroid_h / 2], [asteroid_w, asteroid_h],
                      pos, [asteroid_w, asteroid_h])

    
# create frame and register draw handler    
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")

frame.set_draw_handler(draw)
frame.set_mousedrag_handler(drag)
frame.set_mouseclick_handler(click)

# start frame
frame.start()
        
                                       