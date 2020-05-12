# implementation of card game - Memory

import simplegui
import random

numbers = range(8)*2
w = 800
h = 100
count = 0
win = 0
exposed = [0]*16
state = 0
turn_count = 0


# helper function to initialize globals
def new_game():
    global numbers, turn_count, state, exposed, win
    random.shuffle(numbers)  
    turn_count = 0
    state = 0
    win = 0
    frame.set_canvas_background('Black')
    label.set_text("Turns = " + str(turn_count))
    exposed = [0]*16

        
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, exposed, ind1, ind2, turn_count
    
    if state == 1:
        ind2 = pos[0] / (w/16)
        if exposed[ind2] == 0:
            exposed[ind2] = 1
            state = 2
            turn_count += 1
            label.set_text("Turns = " + str(turn_count))
            
    elif state == 2:
        ind3 = pos[0] / (w/16)
        if exposed[ind3] == 0:
            if numbers[ind1] - numbers[ind2] != 0:
                exposed[ind1] = 0
                exposed[ind2] = 0
            ind1 = ind3
            exposed[ind1] = 1
            state = 1
            
    else:
        ind1 = pos[0] / (w/16)
        exposed[ind1] = 1
        state = 1 
        
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global count, win  
    
    for n in numbers:
        count += 1
        canvas.draw_text(str(n), (count * w/16 - w/24, h/1.8), 28, 'White')
    count = 0
    
    if win == 16:
        frame.set_canvas_background('Maroon')
        win_msg =  "You won, nice! You took " + str(turn_count) + " attempts."
        canvas.draw_text(win_msg, (w/2.75, h/1.2), 14, 'Yellow')
    else:
        win = 0
        for card in exposed:
            count += 1

            if card == 0:
                canvas.draw_line((count * w/16 - w/32, 0), (count * w/16 - w/32, h), 48, 'Green')
            else:
                win +=1	
        count = 0
            
            
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", w, h)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns =" + str(turn_count))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()