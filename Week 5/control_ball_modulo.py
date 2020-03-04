5# control the position of a ball using the arrow keys

import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]

# define event handlers
def draw(canvas):
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    canvas.draw_text(str(ball_pos), [10, 10], 12, "White")

def keydown(key):
    vel = 50
    if key == simplegui.KEY_MAP["left"]:
        ball_pos[0] = (ball_pos[0] - vel) % 600
    elif key == simplegui.KEY_MAP["right"]:
        ball_pos[0] = (ball_pos[0] + vel) % 600
    elif key == simplegui.KEY_MAP["down"]:
        ball_pos[1] = (ball_pos[1] + vel) % 400
    elif key == simplegui.KEY_MAP["up"]:
        ball_pos[1] = (ball_pos[1] - vel) % 400
    
# create frame 
frame = simplegui.create_frame("Positional ball control", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)

# start frame
frame.start()
