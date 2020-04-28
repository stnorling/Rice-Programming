########################
# Incomplete code from Pong
# Repeated code

def draw(c):
    global paddle1_pos, paddle2_pos
    
    paddle_width = 80

    if paddle_width/2 <= paddle1_pos + paddle1_vel <= width - paddle_width/2:
        paddle1_pos += paddle1_vel
    if paddle_width/2 <= paddle2_pos + paddle2_vel <= width - paddle_width/2:
        paddle2_pos += paddle2_vel
        
    c.draw_line([width/2, 0],[width/2, height], 1, "White")
    
    c.draw_line([4, paddle1_pos-paddle_width/2], [4, paddle1_pos+paddle_width/2], 4, "White")
    c.draw_line([width-4, paddle2_pos-paddle_width/2], [width-4, paddle2_pos+paddle_width/2], 4, "White")
    
    ...


########################
# Incomplete code from Pong
# Avoiding repetition with functions

paddle_width = 80
    
def paddle_move(paddle_num):
    if paddle_width/2 <= paddle_pos[paddle_num] + paddle_vel[paddle_num] <= width - paddle_width/2:
        paddle_pos[paddle_num] += paddle_vel[paddle_num]

def paddle_draw(c, paddle_num):
    c.draw_line([paddle_loc[paddle_num], paddle_pos[paddle_num] - paddle_width/2],
                PADDLE_THICKNESS, "White")


def draw(c):
    paddle_move(0)
    paddle_move(1)
    
    c.draw_line([width / 2, 0],[width / 2, height], 1, "White")
 
    paddle_draw(c,0)
    paddle_draw(c,1)
    
    ...


########################
# Incomplete code from Pong
# Avoiding repetition with classes and methods

class Paddle:
    def __init__(self, loc, pos, vel):
        self.loc = loc
        self.pos = pos
        self.vel = vel
        self.width = 80
    
    def move(self):
        if self.width/2 <= self.pos + self.vel <= width - self.width/2:
            self.pos += self.vel
            
    def draw(c, self):
        c.draw_line([self.loc, self.pos-self.width / 2], PADDLE_THICKNESS, "White")

def draw(c):
    paddle1.move()
    paddle2.move()
        
    c.draw_line([width / 2, 0],[width / 2, height], 1, "White")
    
    paddle1.draw(c)
    paddle2.draw(c)
    
    ...


########################
# Incomplete code from Pong
# Long if/elif chain

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= 2
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel += 2
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel -= 2
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel += 2


########################
# Incomplete code from Pong
# Avoiding long if/elif chain with dictionary mapping values to actions

def paddle1_faster():
    global paddle1_vel
    paddle1_vel += 2

def paddle1_slower():
    global paddle1_vel
    paddle1_vel -= 2
    
def paddle2_faster():
    global paddle2_vel
    paddle2_vel += 2    

def paddle2_slower():
    global paddle2_vel
    paddle2_vel -= 2


inputs = {"up": paddle2_slower,
          "down": paddle2_faster,
          "w": paddle1_slower,
          "s": paddle1_faster}


# See below example of dictionary mapping to functions. Very cool!
def keydown(key):
    for i in inputs:
        if key == simplegui.KEY_MAP[i]:
            inputs[i]()


########################
# Illustration of a dictionary mapping values to functions

def f():
    print "hi"

d = {0: f}

d[0]()


########################
# Incomplete code from Pong
# Avoiding long if/elif chain with dictionary mapping values to action arguments

# This is very useful when you want to simplify long conditionals that are repeatedly tracking
# the same variable for different values.

inputs = {"up": [1, -2],
          "down": [1, 2],
          "w": [0, -2],
          "s": [0, 2]}

def keydown(key):
    for i in inputs:
        # key value is a number argument, obtained from the keyhandler. (In dictionary KEY_MAP)
        if key == simplegui.KEY_MAP[i]:
            # Very smartly, inputs[i][0] determines the user paddle (0 or 1). 
            # inputs[i][1] determines if the movement is up or down. the paddle velocity is moved accordingly. 
            paddle_vel[inputs[i][0]] += inputs[i][1]


########################
# Sample of using tiled image
# Has some uses of "magic" (unexplained) constants.

# demo for drawing using tiled images

import simplegui

# define globals for cards
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
SUITS = ['C', 'S', 'H', 'D']

# card sprite - 950x392
# unexplained constants below
CARD_CENTER = (36.5, 49)
CARD_SIZE = (73, 98)
card_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")


# define card class
class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def draw(self, canvas, pos):
        i = RANKS.index(self.rank)
        j = SUITS.index(self.suit)
        card_pos = [CARD_CENTER[0] + i * CARD_SIZE[0],
                    CARD_CENTER[1] + j * CARD_SIZE[1]]
        canvas.draw_image(card_image, card_pos, CARD_SIZE, pos, CARD_SIZE)

# define draw handler        
def draw(canvas):
    one_card.draw(canvas, (155, 90))

# define frame and register draw handler
frame = simplegui.create_frame("Card draw", 300, 200)
frame.set_draw_handler(draw)

# createa card
one_card = Card('S', '6')

frame.start()


########################
# Sample of using tiled image
# Naming constants and calculating other constants from those

# demo for drawing using tiled images

import simplegui

# define globals for cards
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
SUITS = ['C', 'S', 'H', 'D']

# card sprite - 950x392
CARD_SIZE = (73, 98)
card_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

# Rather than putting 'magic' (unnamed) constants in to our code, give them names. This allows for someone to understand 
# what they represent. And secondly, if some constant depends upon another constant, put that computation actually 
# in the code, not just in your brain. Make it explicit so that if you change one part, the other part actually 
# still works (it adjusts accordingly). Example below - creating the FRAME_SIZE tuple variable.
FRAME_SIZE = (300, 200)

# define card class
class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def draw(self, canvas, pos):
        i = RANKS.index(self.rank)
        j = SUITS.index(self.suit)
        # We discard the CARD_CENTER variable all together, as it can be account for in the below formula
        card_loc = [(.5 + i) * CARD_SIZE[0],
                    (.5 + j) * CARD_SIZE[1]]
        canvas.draw_image(card_image, card_loc, CARD_SIZE, pos, CARD_SIZE)

# define draw handler        
def draw(canvas):
    # Frame size variable referenced below, rather than using some arbitrary 'magic' unnamed constants.
    one_card.draw(canvas, (FRAME_SIZE[0] / 2, FRAME_SIZE[1] / 2))

# define frame and register draw handler
frame = simplegui.create_frame("Card draw", FRAME_SIZE[0], FRAME_SIZE[1])
frame.set_draw_handler(draw)

# create a card
one_card = Card('S', '6')

frame.start()


########################
# Incomplete code from Pong
# Magic unnamed constants, repeated code, long expressions

width = 600
height = 400


def ball_init():
    if random.randrange(0,2) == 0:
        return [300,200], [3 + 3 * random.random(), 8 * (random.random() - 0.5)]
    else:
        return [300,200], [-(3 + 3 * random.random()), 8 * (random.random() - 0.5)]


########################
# Incomplete code from Pong
# Constants named and computed, repetition avoided, expressions broken into named pieces.
# Breaking down the long expressions in to parts and assigning them names makes the expression much easier to read
# (both how the expression is computed, and what is being computed)

width = 600
height = 400


def ball_init():
    pos = [width/2, height/2]
    
    vel_x = 3 + 3 * random.random()
    vel_y = 8 * (random.random() - 0.5)
    
    if random.randrange(0,2) == 1:
        vel_x = -vel_x
    
    return pos, [vel_x, vel_y]
