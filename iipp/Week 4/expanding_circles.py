# Expanding circle by timer

###################################################
# Student should add code where relevant to the following.

import simplegui 

WIDTH = 300
HEIGHT = 300
radius = 1
dir = 1


# Timer handler

def tradius():
    global radius, dir
    if radius > 50:
        dir = -1
    elif radius < 2:
        dir = 1
    
    radius += dir
    # print radius
    
# Draw handler

def draw(canvas): 
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2], radius, 1.5, "red")
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2], radius ** 2, 2, "blue")
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2], radius ** 1.75, 3, "pink")
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2], radius ** 0.5, 8, "green")
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2], radius ** 1.5, 5, "yellow")
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2], radius ** 1.2, 1, "white")
    
    canvas.draw_circle([WIDTH / 3, HEIGHT / 2], radius, 2, "red")
    canvas.draw_circle([WIDTH / 3, HEIGHT / 2], radius ** 2, 2, "blue")
    canvas.draw_circle([WIDTH / 3, HEIGHT / 2], radius ** 1.75, 3, "pink")
    canvas.draw_circle([WIDTH / 3, HEIGHT / 2], radius ** 0.5, 8, "green")
    canvas.draw_circle([WIDTH / 3, HEIGHT / 2], radius ** 1.5, 4, "yellow")
    canvas.draw_circle([WIDTH / 3, HEIGHT / 2], radius ** 1.2, 1.5, "white")

    canvas.draw_circle([WIDTH / 1.5, HEIGHT / 2], radius, 1, "red")
    canvas.draw_circle([WIDTH / 1.5, HEIGHT / 2], radius ** 2, 2, "blue")
    canvas.draw_circle([WIDTH / 1.5, HEIGHT / 2], radius ** 1.75, 3, "pink")
    canvas.draw_circle([WIDTH / 1.5, HEIGHT / 2], radius ** 0.5, 8, "green")
    canvas.draw_circle([WIDTH / 1.5, HEIGHT / 2], radius ** 1.5, 5, "yellow")
    canvas.draw_circle([WIDTH / 1.5, HEIGHT / 2], radius ** 1.2, 2, "white")
    
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2], radius ** 1.4, 3, "orange")
    
# Create frame and timer

f = simplegui.create_frame("Radius", WIDTH, HEIGHT, 60)
t = simplegui.create_timer(100, tradius)
                           
f.set_draw_handler(draw)

# Start timer

f.start()
t.start()