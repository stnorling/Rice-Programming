# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
vel = 4

# initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel = [0, 0]
    if direction == RIGHT:
        ball_vel = [random.randrange(3, 5), -random.randrange(1, 3)]    
    elif direction == LEFT:
        ball_vel = [-random.randrange(3, 5), -random.randrange(1, 3)]    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    paddle1_pos, paddle2_pos = HEIGHT / 2, HEIGHT / 2
    paddle1_vel, paddle2_vel = 0, 0
    score1, score2 = 0, 0
    spawn_ball(LEFT)

    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if ball_pos[1] < BALL_RADIUS or ball_pos[1] > (HEIGHT - BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # Debug values of ball_pos and ball_vel
    #canvas.draw_text(str(ball_pos), [10, 10], 12, 'White')
    #canvas.draw_text(str(ball_vel), [10, 20], 12, 'White')
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'White', 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + paddle1_vel <= HEIGHT - HALF_PAD_HEIGHT and paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    
    if paddle2_pos + paddle2_vel <= HEIGHT - HALF_PAD_HEIGHT and paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT:
        paddle2_pos += paddle2_vel
     
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], 
                     [HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], 
                     PAD_WIDTH, 'White')
    
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], 
                     [WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], 
                     PAD_WIDTH, 'White')
    
    # determine whether paddle and ball collide    
    if abs(paddle1_pos - ball_pos[1]) <= abs(PAD_HEIGHT / 2) and ball_pos[0] < PAD_WIDTH + BALL_RADIUS:
        ball_vel[0] = - ball_vel[0] * 1.10
    elif ball_pos[0] < PAD_WIDTH + BALL_RADIUS:
        score2 += 1
        spawn_ball(RIGHT)
    
    if abs(paddle2_pos - ball_pos[1]) <= abs(PAD_HEIGHT / 2) and ball_pos[0] > WIDTH - PAD_WIDTH - BALL_RADIUS:
        ball_vel[0] = - ball_vel[0] * 1.10
    elif ball_pos[0] > WIDTH - PAD_WIDTH - BALL_RADIUS:
        score1 += 1
        spawn_ball(LEFT)
    
    # draw scores
    
    canvas.draw_text(str(score1), [WIDTH * 0.25, HEIGHT / 2], 30, 'White')
    canvas.draw_text(str(score2), [WIDTH * 0.75, HEIGHT / 2], 30, 'White')
  

def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = vel
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel = -vel
        
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = vel
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -vel
  

def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['s'] or key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['up'] or key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
    

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Reset', new_game, 50)


# start frame
new_game()
frame.start()
