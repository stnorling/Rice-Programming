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

# helper functions

import random

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
        exit()
        
    # convert name to number using if/elif/else
    # don't forget to return the result!


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
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    
    print ""
    print "Player's choice: " + player_choice

    player_num = name_to_number(player_choice)

    comp_num = random.randrange(0, 5)
    comp_choice = number_to_name(comp_num)
    
    print "Computer's choice: " + comp_choice

    differential = (player_num - comp_num) % 5

    if differential == 0:
        print "Player and computer tie!"
    elif differential < 3:
        print player_choice + " beats " + comp_choice + ". Player wins!"
    else:
        print comp_choice + " beats " + player_choice + ". Computer wins!"

    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
rpsls("yolo")

# always remember to check your completed program against the grading rubric


