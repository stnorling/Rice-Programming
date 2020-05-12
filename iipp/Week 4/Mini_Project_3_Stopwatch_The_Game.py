# template for "Stopwatch: The Game"

import simplegui

# define global variables

count = 0
height = 200
width = 200
a, b, c, d = 0, 0, 0, 0
x, y = 0, 0
new = False
score = "0/0"

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global a, b, c, d
    d = t % 10
    c = (t % 100) / 10
    b = (t % 600) / 100
    a = t / 600
    ft = str(a) + ":" + str(b) + str(c) + "." + str(d)
    return ft
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    global new
    t.start()
    new = True
    
def stop():
    global x, y, new, score
    t.stop()
    if new == True:
        y += 1
        if count % 10 == 0:
            x += 1
    new = False
    score = str(x) + "/" + str(y) 
    
def reset():
    global count, x, y, score
    t.stop()
    count, x, y = 0, 0, 0
    score = str(x) + "/" + str(y)

# define event handler for timer with 0.1 sec interval

def timer():
    global count
    count += 1

# define draw handler

def draw(canvas):
    canvas.draw_text(format(count), [height / 2.5, width / 2], 18, 'White')
    canvas.draw_text(score, [height / 1.2, width / 5], 14, 'White')
        
# create frame

f = simplegui.create_frame("Stopwatch", height, width)

# register event handlers

f.set_draw_handler(draw)
f.add_button("Start", start, 50)
f.add_button("Stop", stop, 50)
f.add_button("Reset", reset, 50)

t = simplegui.create_timer(100, timer)

# start frame

f.start()

# Please remember to review the grading rubric

print format(3465)
print format(613)
print format(36000)
