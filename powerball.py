# Compute and print powerball numbers.

###################################################
# Powerball function
# Student should enter function on the next lines.

import random

def rn():
    return random.randrange(1,60)

def powerball():
    pb = random.randrange(1, 36)
    print "Today's numbers are " + str(rn()) + " " + \
    str(rn()) + " " + str(rn()) + " " + str(rn()) + " " + \
    str(rn()) + ". The Powerball number is " + str(pb) + "."
    
###################################################
# Tests
# Student should not change this code.
    
powerball()
powerball()
powerball()
