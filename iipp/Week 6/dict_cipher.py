# Cipher

import simplegui
import random

LETTERS = "abcdefghijklmnopqrstuvwxyz"
CIPHER = {}

message = ""

def init():
    letters_list = list(LETTERS)
    # list shuffle method creates a random pemutation
    # of the contents of the list.
    random.shuffle(letters_list)
    for l in LETTERS:
        CIPHER[l] = letters_list.pop()
    

# Encode button
def encode():
    emsg = ""
    for ch in message:
        emsg += CIPHER[ch]
    print message, "encodes to", emsg
    

# Decode button
def decode1():
    dmsg = ""
    for ch in message:
        # Dictionary .items() method returns a list of 
        # (key, value) pairs for all pairs in the dictionary.
        for key, value in CIPHER.items():
            if ch == value:
                dmsg += key
    print message, "decodes to", dmsg

    
# Update message input
def newmsg(msg):
    global message
    message = msg
    label.set_text(msg)
    
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Cipher", 2, 200, 200)
frame.add_input("Message:", newmsg, 200)
label = frame.add_label("", 200)
frame.add_button("Encode", encode)
frame.add_button("Decode", decode1)

# Start the frame animation
frame.start()
init()