# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors


# GUI-based version of RPSLS

###################################################

import simplegui
import random

# Functions that compute RPSLS

# helper functions

def name_to_number(name):
    
    if name == 'rock':
        return 0
    elif name == 'Spock' or name =='spock':
        return 1
    elif name == 'paper':
        return 2        
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        print "Invalid selection: " + str(name) + ". Please try again."
        return None
        

def number_to_name(number):
   
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    else:
        return 'scissors'

# main function

def rpsls(player_choice): 
    
    print ""
    print "Player's choice: " + player_choice

    player_num = name_to_number(player_choice)
    
    if player_num == None:
        return None

    comp_num = random.randrange(0, 5)
    comp_choice = number_to_name(comp_num)
    
    print "Computer's choice: " + comp_choice

    differential = (player_num - comp_num) % 5

    if differential == 0:
        print "Player's draw!"
    elif differential < 3:
        print player_choice + " beats " + comp_choice + ". Player wins!"
    else:
        print comp_choice + " beats " + player_choice + ". Computer wins!"
    
    
# Handler for input field
def get_guess(guess):
    rpsls(guess)
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 200, 200)
frame.add_input("Enter guess for RPSLS", get_guess, 200)


# Start the frame animation
frame.start()


###################################################
# Test

get_guess("Spock")
get_guess("dynamite")
get_guess("paper")
get_guess("lazer")

###################################################
# Sample expected output from test
# Note that computer's choices may vary from this sample.

#Player chose Spock
#Computer chose paper
#Computer wins!
#
#Error: Bad input "dynamite" to rpsls
#
#Player chose paper
#Computer chose scissors
#Computer wins!
#
#Error: Bad input "lazer" to rpsls
#