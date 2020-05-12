# Move a ball

###################################################
# Student should add code where relevant to the following.


import simplegui 

# Define globals - Constants are capitalized in Python
HEIGHT = 400
WIDTH = 400
RADIUS_INCREMENT = 5
ball_radius = 20
change = 1

# Draw handler

def draw(canvas):
    canvas.draw_circle([HEIGHT / 2, WIDTH / 2], ball_radius, 2, "white")
    
# Event handlers for buttons

def increase_radius():
    global ball_radius
    ball_radius += change    
    
def decrease_radius():
    global ball_radius
    if ball_radius - change < 1:
        print "Can't make the radius smaller by that amount!"
    else:
        ball_radius -= change
        
def reset():
    global ball_radius
    ball_radius = 20
    
def custom_radius(r):
    global ball_radius
    ball_radius = int(r)
    
def change_amt(i):
    global change
    change = int(i)
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Ball control", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button("Increase radius", increase_radius)
frame.add_button("Decrease radius", decrease_radius)
frame.add_button("Reset radius", reset)
frame.add_input("Enter radius", custom_radius, 50)
frame.add_input("Enter radius change amount", change_amt, 50)


# Start the frame animation
frame.start()

