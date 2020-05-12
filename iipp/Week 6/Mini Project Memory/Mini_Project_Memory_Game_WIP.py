# implementation of card game - Memory

import simplegui
import random

numbers = range(8)*2
w = 800
h = 100
count = 0
exposed = [0]*16
state = 0

# helper function to initialize globals
def new_game():
    global numbers
    random.shuffle(numbers)  

# FOR TOMORROW: YOU'RE LOOKING AT IT WRONG. RATHER THAN COMPARING 
# IND1 AND IND2, CHECK WHETHER THE EXPOSED[ ] IS 1 OR 0.
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, exposed, ind1, ind2
    
    if state == 0:
        ind1 = pos[0] / (w/16)
        exposed[ind1] = 1
        state = 1
        
    if state == 1:
        ind2 = pos[0] / (w/16)
        if ind2 != ind1:
            if exposed[ind2] == 0:
                exposed[ind2] = 1
                state = 2
            print ind1, ind2, "State 2 entered"
            
    else:
        if exposed[pos[0] / (w/16)] == 0:
            if numbers[ind1] - numbers[ind2] != 0:
                exposed[ind1] = 0
                exposed[ind2] = 0
            ind1 = pos[0] / (w/16)
            exposed[ind1] = 1
            state = 1
            print ind1, ind2, "State 1 entered"
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global count   
    for n in numbers:
        count += 1
        canvas.draw_text(str(n), (count * w/16 - w/24, h/1.8), 28, 'White')
    count = 0
    for card in exposed:
        count += 1
        if card == 0:
            canvas.draw_line((count * w/16 - w/32, 0), (count * w/16 - w/32, h), 48, 'Green')
    count = 0
            
            

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", w, h)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

print numbers
# Always remember to review the grading rubric