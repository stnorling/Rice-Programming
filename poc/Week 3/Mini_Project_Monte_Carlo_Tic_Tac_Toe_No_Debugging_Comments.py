"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 100        # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 2.0   # Score for squares played by the other player
    
# Add your functions here.

def mc_trial(board, player):
    """
    Simulates a game starting with the given player by making
    random moves, alternating between players. Board input is
    modified, and returns when the game is over.
    """
    while board.check_win() == None:
        tmove = random.choice(board.get_empty_squares())
        board.move(tmove[0], tmove[1], player)
        player = provided.switch_player(player)
    return True
    
    
def mc_update_scores(scores, board, player):
    """
    Scores a completed board and updates the scores grid.
    Player is which player the machine is. Doesn't return anything.
    """
    winner = board.check_win()
    if winner == provided.DRAW or winner == provided.EMPTY:
        return None
    dim = board.get_dim()
    for row in range(dim):
        for col in range(dim):
            if board.square(row, col) != provided.EMPTY:
                if player == winner:
                    if board.square(row, col) == winner:
                        scores[row][col] += SCORE_CURRENT
                    else: scores[row][col] -= SCORE_OTHER
                else:
                    if board.square(row, col) == winner:
                        scores[row][col] += SCORE_OTHER
                    else: scores[row][col] -= SCORE_CURRENT
                
                
def get_best_move(board, scores):
    """
    Finds all empty squares with the maximum score and randomly
    returns one of them as a (row, column) tuple. 
    """
    possible_moves = board.get_empty_squares()
    best_moves = []
    best_score = None
    for idx in possible_moves:
        score = scores[idx[0]][idx[1]]
        if score > best_score:
            best_score = score
            best_moves = [idx]
        elif score == best_score:
            best_moves.append(idx)
    return random.choice(best_moves)

    
def mc_move(board, player, trials):
    """
    Takes a current board, which player the machine is, and the number
    of trials to run. Uses Monte Carlo simulation to return a move for
    the machine player in the form of a (row, column) tuple. 
    """
    dim = board.get_dim()
    scores = [[0 for dummy_col in range(dim)] for dummy_row in range(dim)]
    for dummy_trial in range(trials):
        board_copy = board.clone()
        mc_trial(board_copy, player)
        mc_update_scores(scores, board_copy, player)
    return get_best_move(board, scores)
    
    
# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

def ttt_test_suite():
    """
    Test suite for tic tac toe Monte Carlo implementation.
    """
    board1 = provided.TTTBoard(3)
    print board1.get_dim()
    print board1
    print mc_trial(board1, provided.PLAYERX)
    print board1
    print '-----------------'
    board2 = provided.TTTBoard(3)
    next_move = mc_move(board2, provided.PLAYERX, 10)
    print next_move
    print board2
    board2.move(next_move[0], next_move[1], provided.PLAYERX)
    print board2
    
#ttt_test_suite()