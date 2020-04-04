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
UNICORNS = (255675, 860767, 922983, 878635, 77509, 435524, 231671, 177223, 939998)
Found = False
sx = random.randrange(800)
sy = random.randrange(100)
print (sx,sy)
#here is the unicorn hunter for anyone intersted
# http://www.codeskulptor.org/#user47_Vs8CoTZHhG_1.py
#

## I wanted borders on my cards so set up a list of card corners
## card[[x,y],[x,y],[x,y],[x,y]]

cards = []
for i in range(16):
    x=i*50+7
    cards.append([[x-5, 5], [x+40,5 ], [x+40,95], [x-5, 95]])


# helper function to initialize globals
def new_game():
    global deck
    global exposed
    global uni
    global num_up
    global round
    global turn
    global Found
    
    if turn == 0:
        Found = False
        label2.set_text("")
        
        
    round = [0,0]
    num_up = 0
    turn = 0
    label.set_text("Turns = %d"%turn)
    
    if Found:
        secret_number = UNICORNS[uni]  
        uni += 1
        if uni == 9 : uni = 0
    else:
        secret_number = random.randrange(0,1000000)
    random.seed(secret_number)
    #print('xx:',secret_number)
    
    #build deck 
    deck = [card for card in range(8)  for trip in range(2)]
    random.shuffle(deck)
    #exposed = [x%2==0  for x in range(16)]
    exposed = [False  for x in range(16)]

#    #debug Stuff
#    print (deck)
#    print (exposed)
#    print "\n"
    
def where(click):
    for i in range(16):
        card = cards[i]
        print(click,card)
        cx1 = card[0][0]
        cy1 = card[0][1]
        cx2 = card[2][0]
        cy2 = card[2][1]
        #print(cx1,cy1,cx2,cy2)
        #print(click)
        if (click[0] > cx1 and click[0] < cx2) and \
            (click[1] > cy1 and click[1] < cy2):
            return i
    return -1     

def match():
    return deck[round[0]] == deck[round[1]]

def unicorn_check(pos):
    global Found
    if (pos == (sx,sy)) or (pos == (sx+1,sy+1)) or (pos == (sx-1,sy-1)) or (pos == (sx+1,sy-1)) or (pos == (sx-1,sy+1)):
        Found = True
        print 'Unicorn found'
        label2.set_text("Rainbows and sprnkles")
    
# define event handlers
def mouseclick(pos):
    global exposed
    global num_up
    global round
    global turn
    
    unicorn_check(pos)
        
    choice = where(pos)
    debug = -1    
    if choice > -1:
        i = choice
        debug = i
        if num_up == 0:
            exposed[i] = not exposed[i]
            num_up = 1
            round[0] = i
        
        elif num_up == 1:
            if exposed[i]:
                pass
            else:
                exposed[i] = not exposed[i]
                num_up = 2
                round[1] = i
                turn += 1
                label.set_text("Turns = %d"%turn)
        else:
            if exposed[i]:
                pass
            else:
                num_up = 1
                exposed[i] = not exposed[i]
                if match():
                    round[0] = i
                else:                    
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
#            
       
                   
                   
# cards are logically 50x100 pixels in size    
def draw(canvas):
    y=60
    for i in range(16):
        x=i*50+7
        canvas.draw_text(str(deck[i]), (x+9, y), 40, 'Aqua')
        if exposed[i]:
            canvas.draw_polygon(cards[i], 2, 'Yellow')
        else:
            canvas.draw_polygon(cards[i], 2, 'Yellow', 'Orange')
        
    canvas.draw_circle((sx, sy), 1, 1, 'Green')   
 
   


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