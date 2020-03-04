# Ball motion with an implicit timer

# In the below there is no explicit timer. The ball position is 
# updated as per the velocity each time the draw handler event 
# is called (60 times a second). 

# The position is updated per increment by the velocity we have set
# which we can change for given values. E.g. we could run an if
# statement to change the direction of the ball position movement. 

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
vel = [-2, 1] # pixels per update (1/60 seconds)

# define event handlers
def draw(canvas):
    # Update ball position
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]

    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

# create frame
frame = simplegui.create_frame("Motion", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()
