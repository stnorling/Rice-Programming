# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

guesses = 7
count = 0
rg1000 = False
secret_number = 0
numrange = 100

# helper function to start and restart the game

def remaining_guesses():
    global guesses, count
    count = count + 1
    guesses = guesses - 1
    if guesses == 0:
        print "You are out of guesses. Game over! \nThe number was", secret_number, "\n"
        if rg1000 == False:
            new_game()
        else:
            range1000()
    else:
        print "You have " + str(guesses) + " guesses left.\n"

def new_game():
    # initialize global variables used in your code here
    global secret_number, count, rg1000
    count = 0  
    secret_number = random.randrange(0, numrange)
    
    if rg1000 == False:
        print "New game - pick a number between 0 and 99"
    else:
        print "New game - pick a number between 0 and 999"
        
    print "You have " + str(guesses) + " remaining guesses.\n"


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global numrange, guesses, rg1000
    
    rg1000 = False
    numrange = 100
    guesses = 7   
    
    new_game()
  

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global numrange, guesses, rg1000
    
    rg1000 = True
    numrange = 1000
    guesses = 10

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
