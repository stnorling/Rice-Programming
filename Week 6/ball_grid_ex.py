# Ball grid slution

###################################################
# Student should enter code below

import simplegui

BALL_RADIUS = 20
GRID_SIZE = 10
WIDTH = 2 * GRID_SIZE * BALL_RADIUS
HEIGHT = 2 * GRID_SIZE * BALL_RADIUS
GRID_SIZE_PLUS = GRID_SIZE + 1

# define draw
           
               
def draw(canvas):
    for i in range(1, GRID_SIZE_PLUS):
        for j in range(1, GRID_SIZE_PLUS):
            pos =  WIDTH - (i * (WIDTH/GRID_SIZE_PLUS)), HEIGHT - (j * (HEIGHT/GRID_SIZE_PLUS))
            canvas.draw_circle(pos, BALL_RADIUS, 1, "Green", "Green")
   

# create frame and register handlers
frame = simplegui.create_frame("Ball grid", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# start frame
frame.start()
#test()
