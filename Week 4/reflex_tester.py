# Reflex tester

###################################################
# Student should add code where relevant to the following.

import simplegui 

total_ticks = 0
first_click = True


# Timer handler

def tick():
    global total_ticks
    if first_click:
        total_ticks += 10        
    
# Button handler

def click():
    global first_click, total_ticks
    if first_click:
        first_click = False
        print "Reflex ticks:", total_ticks
        if total_ticks < 100:
            print "What a beast calm down mate"
    else:
        print "Go!"
        first_click = True
        total_ticks = 0


# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Click me", click, 200)
timer = simplegui.create_timer(10, tick)

# Start timer
frame.start()
timer.start()
print "Go!"