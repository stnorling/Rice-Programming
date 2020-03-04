import simplegui

# Initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20

ball_pos = [WIDTH / 2, HEIGHT / 2]
# vel = [-40.0 / 60.0,  5.0 / 60.0]
vel = [-4, 3]

# define event handlers
def draw(canvas):
    
    # By drawing the velocity on to the canvas we can see
    # how velocity changes direciton as the ball collides with
    # the edges of the canvas.
    
    canvas.draw_text(str(vel), [5, 15], 12, 'White')

    # Update ball position
    
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]
    
    # collide and reflect off of sides of the canvas each time the 
    # ball hits the edge. Do this by simply changing the direction
    # of the axis velocity when it hits the edge of the canvas
    
    if ball_pos[0] <= BALL_RADIUS:
        vel[0] = - vel[0]
        
    if ball_pos[0] > WIDTH - BALL_RADIUS:
        vel[0] = - vel[0]
        
    if ball_pos[1] < BALL_RADIUS:
        vel[1] = - vel[1]
        
    if ball_pos[1] > HEIGHT - BALL_RADIUS:
        vel[1] = - vel[1]

    # Draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")

# create frame
frame = simplegui.create_frame("Ball physics", WIDTH, HEIGHT)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()
