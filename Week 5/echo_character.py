# Keyboard echo

# Note: Key downs override each other. E.g. hold down one, then another,
# the new key triggers the keydown event and becomes the current key.

# If holding down two keys and release one, this triggers the key up event.

import simplegui

# initialize state
current_key = ' '

# event handlers
def keydown(key):
    global current_key
    current_key = chr(key)
    print chr(key)
    print key
    
def keyup(key):
    global current_key
    current_key = ' '
    
def draw(c):
    # NOTE draw_text now throws an error on some non-printable characters
    # Since keydown event key codes do not all map directly to
    # the printable character via ord(), this example now restricts
    # keys to alphanumerics
    
    if current_key in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        c.draw_text(current_key, [10, 25], 20, "Red")    
        
# create frame             
f = simplegui.create_frame("Echo", 35, 35)

# register event handlers
f.set_keydown_handler(keydown)
f.set_keyup_handler(keyup)
f.set_draw_handler(draw)

# start frame
f.start()