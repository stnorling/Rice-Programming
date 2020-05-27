"""
Student facing implement of solitaire version of Mancala - Tchoukaillon

Goal: Move as many seeds from given houses into the store

In GUI, you make ask computer AI to make move or click to attempt a legal move
"""


class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """
    
    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self.board = [0]
    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        self.board = list(configuration)
    
    def __str__(self):
        """
        Return string representation for Mancala board
        """
        return str(self.board)
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return self.board[house_num]

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        return True
    
    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
        return True

    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        pass

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        return 0
    
    def plan_moves(self):
        """
        Return sequence of shortest legal moves until none are available
        Not used in GUI version, only for machine testing
        """
        return []
 
# import test suite and run
import poc_mancala_testsuite_v2 as poc_mancala_testsuite
poc_mancala_testsuite.run_suite(SolitaireMancala)
    

