# implementation of card game - Memory

''' 
    IMPORTANT NOTICE

IF you see "Rainbows and sprinkles"
UNICORN MODE = Activated
Clicking Reset with Turns = 0 will DeActivate

    IMPORTANT NOTICE
'''

import simplegui
import random
turn = 0

#setup cheat mode based on conspiracy theory launched in videos
uni=0
# UNICORNS are the random seed numbers that result in a number set with 5 or more 
# pairs of numbers in a row. (Results in a very low turn count game). Note, there
# are many more of these seed numbers than the numbers listed below.
UNICORNS = (255675, 860767, 922983, 878635, 77509, 435524, 231671, 177223, 939998)
Found = False
# Below are the coordinates used to activate Unicorn mode when they're clicked on.
sx = random.randrange(800)
sy = random.randrange(100)
print (sx,sy)

# here is the unicorn hunter for anyone intersted
# http://www.codeskulptor.org/#user47_Vs8CoTZHhG_1.py

## I wanted borders on my cards so set up a list of card corners
## card[[x,y],[x,y],[x,y],[x,y]]

cards = []
for i in range(16):
    x=i*50+7
    # each list of card corners is a list of 4 sublists, each sublist being corner
    # coordinates per each of the 16 cards. This is appended to the list 'cards'.
    cards.append([[x-5, 5], [x+40,5 ], [x+40,95], [x-5, 95]])
    #print cards
    print cards[0]
    
# helper function to initialize globals
def new_game():
    global deck
    global exposed
    global uni
    global num_up
    global round
    global turn
    global Found
    
    # sets the unicorn label to "" if previously exposed, turns off Unicorn mode
    # by setting Found to False.
    if turn == 0:
        Found = False
        label2.set_text("")
        
        
    round = [0,0]
    num_up = 0
    turn = 0
    # in string formatting below, we use %d (decimal) as turn is a number.
    label.set_text("Turns = %d"%turn)
    
    # Found == True implies Unicorn mode has been activated. Our number passed in to 
    # random.seed() is a number from our UNICORNS list. As it's a UNICORN number, 
    # random.seed(secret_number) ensures that when we shuffle our deck using 
    # random.shuffle(deck), it returns a set of numbers in which there are 5 or
    # more pairs of numbers that occur one after the other (resulting in a low turn
    # game).
    if Found:
        secret_number = UNICORNS[uni]  
        uni += 1
        if uni == 9 : uni = 0
    else:
        # if Found is False, e.g. we are not in Unicorn mode, a random number is 
        # returned as the argument for random.seed() (which is similar to how random
        # usually works without setting a seed). 
        secret_number = random.randrange(0,1000000)
    random.seed(secret_number)
    #print('xx:',secret_number)
    
    #build deck 
    # Using a second for loop in our list comprehensions ensures our first loop
    # runs twice. (Basically a nested for loop). 
    deck = [card for card in range(8)  for trip in range(2)]
    random.shuffle(deck)
    # We use list comprehension to build our exposed list, containing 16 elements
    # of False. 
    exposed = [False for x in range(16)]

#    #debug Stuff
#    print (deck)
#    print (exposed)
#    print "\n"
    
def where(click):
    for i in range(16):
        # Below iterates per each card in our cards list. Each card[i]
        # is a list of the ith card's corner x and y coordinates
        card = cards[i]
        #print(click,card)
        
        # Below returns the card's two x and y coordinates. 
        cx1 = card[0][0]
        cy1 = card[0][1]
        cx2 = card[2][0]
        cy2 = card[2][1]
        #print(cx1,cy1,cx2,cy2)
        #print(click)
        # Below checks where we clicked. It cycles through each card
        # from left to right, checking if the click is within it's x and
        # y coordinates. If it is, it returns that card's index (i). If 
        # it isn't, it cycles to the next card.
        if (click[0] > cx1 and click[0] < cx2) and \
            (click[1] > cy1 and click[1] < cy2):
            #print i
            return i
    # If the click doesn't sit within any of the card's x and y coordinates,
    # (e.g. out of the boundary), then -1 is returned.
    return -1     

def match():
    # Using our two current indexes, match compares if the values in our deck
    # are the same for the given indexes. Returns True if so.
    return deck[round[0]] == deck[round[1]]

def unicorn_check(pos):
    global Found
    if (pos == (sx,sy)) or (pos == (sx+1,sy+1)) or (pos == (sx-1,sy-1)) \
    or (pos == (sx+1,sy-1)) or (pos == (sx-1,sy+1)):
        Found = True
        print 'Unicorn found'
        label2.set_text("Rainbows and sprinkles")
    
# define event handlers
def mouseclick(pos):
    global exposed
    global num_up
    global round
    global turn
    
    # Below function runs per click. It checks whether pos == the coordinates that
    # activate unicorn mode. If they are, unicorn mode is activated.
    unicorn_check(pos)
    
    # Below runs the helper function where() which determines which card
    # was selected, and returns the card's index number.
    choice = where(pos)
    debug = -1    
    
    # as where(pos) returns -1 if the click is outside any of the card's
    # borders, none of the below code runs when we click outside of the
    # card's borders (nothing happens). 
    if choice > -1:
        i = choice
        debug = i
        # num_up determines the games state (initializes as 0). 
        if num_up == 0:
            # Below changes exposed[i] from False to True
            exposed[i] = not exposed[i]
            # game state is changed to state 1
            num_up = 1
            # round is a list containing the two coordinates of our most
            # recent clicks. Initializes as [0, 0].
            round[0] = i
        
        # if game state (num_up) is 1, the below runs.
        elif num_up == 1:
            # if the selected card is already exposed, (is True), nothing happens.
            if exposed[i]:
                pass
            # if the card is not already exposed, the below runs.
            else:
                # the card becomes exposed and the game state is set to 2. 
                exposed[i] = not exposed[i]
                num_up = 2
                # Our second index is inserted in to round.
                round[1] = i
                # the turn counter is incremented.
                turn += 1
                label.set_text("Turns = %d"%turn)
        # below run when game state (num_up) is 2.
        else:
            # again if selected card is already exposed, nothing happens.
            if exposed[i]:
                pass
            else:
                # game state changes to 1, and the selected card is exposed.
                num_up = 1
                exposed[i] = not exposed[i]
                # below runs the match helper function, which returns True if
                # the two most recently selected cards in the deck are equal.
                if match():
                    # When True, the newly selected card is added in to our index list.
                    round[0] = i
                else:      
                    # When False (e.g. not a match), the previously selected cards
                    # are flipped back to False, and the newly selected card's index  is added
                    # to round.
                    exposed[round[0]] = not exposed[i]
                    exposed[round[1]] = not exposed[i]                    
                    round[0] = i
                    

#	#Debug Stuff
#    print "Card: %d" %debug
#    print "num_up: %d" %num_up
#    print "deck[debug] %d" %deck[debug]
#    print deck[round[0]] , deck[round[1]]
#    print deck[round[0]] == deck[round[1]]
#    print round
#    print        
                   
                   
# cards are logically 50x100 pixels in size    
def draw(canvas):
    y=60
    for i in range(16):
        x=i*50+7
        canvas.draw_text(str(deck[i]), (x+9, y), 40, 'Aqua')
        # Below draws different polygons based on whether our cards are 
        # exposed or not. If they are, it draws a yellow border. If they are
        # not exposed, it fills the yellow border with orange so that you can
        # not see the number beneath. 
        if exposed[i]:
            # cards[i] indexes our cards and returns the ith card's 4 corners,
            # e.g. for card 0: [[2, 5], [47, 5], [47, 95], [2, 95]]. This point
            # list is the first argument for draw_polygon(). 
            canvas.draw_polygon(cards[i], 2, 'Yellow')
        else:
            canvas.draw_polygon(cards[i], 2, 'Yellow', 'Orange')
    # Below draws the point that when clicked activates Unicorn mode.    
    canvas.draw_point((sx, sy), 'Green')   
 
   
   
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")
label2 = frame.add_label("")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric