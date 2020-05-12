import simplegui

def timer1_handler():
    print "1"
    
def timer2_handler():
    print "2"

# by assigning to variables we create timer objects
t1 = simplegui.create_timer(100, timer1_handler)
t2 = simplegui.create_timer(300, timer2_handler)

print(type(t1))

# now that we have timer objects, we can use their methods
t1.start()
t2.start()
