import simplegui

n = 5
c = 0

def keydown(k):
    global n
    n *= 2
    
def keyup(k):
    global n, c
    n -= 3
    c += 1
    if c == 12:
        print "Here's your number G:", n

def draw(canvas):
    canvas.draw_text(str(n), (100, 100), 10, 'White')
    canvas.draw_text(str(c), (10, 10), 10, 'White')
    
f = simplegui.create_frame("Frame", 200, 200)

f.set_draw_handler(draw)
f.set_keydown_handler(keydown)
f.set_keyup_handler(keyup)

f.start()