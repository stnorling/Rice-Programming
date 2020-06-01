"""
A simple Monte Carlo solver for Nim
http://en.wikipedia.org/wiki/Nim#The_21_game
"""

import random
import codeskulptor
codeskulptor.set_timeout(20)

MAX_REMOVE = 3
TRIALS = 10000
bot = True

def evaluate_position(num_items):
    """
    Monte Carlo evalation method for Nim
    """
    move_score = [0 for num in range(MAX_REMOVE)]
    possible_moves = range(1, MAX_REMOVE + 1)
    for first_move in possible_moves:
        for dummy_trial in range(TRIALS):
            idx = possible_moves.index(first_move)
            items = num_items
            items -= first_move
            bot = False
            while items > 0:
                if bot:
                    choice = random.choice(possible_moves)
                    items -= choice
                    bot = False
                else:
                    items -= random.choice(possible_moves)
                    bot = True
            if not bot:
                move_score[idx] += 1
    print move_score
    return move_score.index(max(move_score)) + 1


def play_game(start_items):
    """
    Play game of Nim against Monte Carlo bot
    """
    
    current_items = start_items
    print "Starting game with value", current_items
    while True:
        comp_move = evaluate_position(current_items)
        current_items -= comp_move
        print "Computer choose", comp_move, ", current value is", current_items
        if current_items <= 0:
            print "Computer wins"
            break
        player_move = int(input("Enter your current move"))
        current_items -= player_move
        print "Player choose", player_move, ", current value is", current_items
        if current_items <= 0:
            print "Player wins"
            break

play_game(21)
        
    
                 
    