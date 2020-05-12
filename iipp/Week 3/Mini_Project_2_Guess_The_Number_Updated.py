# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

guesses = 7
count = 0
secret_number = 0
high, low = 100, 0

# helper function to start and restart the game

def remaining_guesses():
    global guesses, count
    count = count + 1
    guesses = guesses - 1
    if guesses == 0:
        print "You are out of guesses. Game over! \nThe number was", secret_number, "\n"
        new_game()
    else:
        print "You have " + str(guesses) + " remaining guesses.\n"

def new_game():
    # initialize global variables used in your code here
    global secret_number, count, guesses
    count = 0  
    secret_number = random.randrange(low, high)
    guesses = int(math.ceil(math.log(high - low, 2)))
    
    print "New game - pick a number between 0 and", high
    print "You have " + str(guesses) + " remaining guesses.\n"


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global high
    high = 100 
    
    new_game()
  

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global high
    high = 1000

    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    num_guess = int(guess)
    
    if num_guess < secret_number:
        print "You picked " + str(num_guess) + ". Higher!"
        remaining_guesses()
    elif num_guess > secret_number:
        print "You picked " + str(num_guess) + ". Lower!"
        remaining_guesses()
    else:
        print "You picked " + str(num_guess) + ". Correct!!!\n"
        if count == 0:
            print "First guess! What a legend!!!\n"
        new_game()

    
# create frame

f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame

f.add_button("New game range is [0, 100)", range100)
f.add_button("New game range is [0, 1000)", range1000)
f.add_input("Enter guess here", input_guess, 50)

f.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
