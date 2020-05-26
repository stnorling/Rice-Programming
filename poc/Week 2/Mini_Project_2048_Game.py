"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    def slide(line):
        """
        Function that slides across numbers from right to left if there are zeroes
        """
        for num in range(len(line) -1):
            if line[num] == 0:
                for tile in range(num, len(line)):
                    if line[tile] > 0:
                        line[num] += line[tile]
                        line[tile] = 0
                        break
        return line

    def inmerge(line):
        """
        Function that merges a single row or column in 2048.
        """    
        new_line = slide(list(line))
        for num in range(len(new_line) - 1):
            if new_line[num] == new_line[num + 1]:
                new_line[num] += new_line[num + 1]
                new_line[num + 1] = 0
                slide(new_line)     
        return new_line

    line_1 = slide(line)
    line_2 = inmerge(line_1)
    return line_2


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, height, width):
        """
        Initialises the game by setting board dimensions and calling reset
        """
        self._grid_height = height
        self._grid_width = width
        self._grid = []
        self.reset()
        self._edge_indices = {UP: [(0, col) for col in range(self.get_grid_width())],
                             DOWN: [(self.get_grid_height() - 1, col) for col in range(self.get_grid_width())],
                             LEFT: [(row, 0) for row in range(self.get_grid_height())],
                             RIGHT: [(row, self.get_grid_width() - 1) for row in range(self.get_grid_height())]
                            }

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in range(self.get_grid_width())]
                     for dummy_row in range(self.get_grid_height())]
        for dummy in range(2):
            self.new_tile()
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        grid_str = ""
        for row in range(self.get_grid_height()):
            grid_str += str(self._grid[row]) + "\n"
        return grid_str

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        prior_grid = str(self)
        edge_tiles = self._edge_indices[direction]
        # determining how far to iterate when offsetting to determine indexes
        iter_length = {UP: self.get_grid_height(),
                   DOWN: self.get_grid_height(),
                   LEFT: self.get_grid_width(),
                   RIGHT: self.get_grid_width()
                   }
        # iterating by edge tile
        for tile in range(len(edge_tiles)):
            line = []
            indices = []
            # gathering indices of each tile in the line
            for ind in range(iter_length[direction]):
                indices.append((edge_tiles[tile][0] + ind * OFFSETS[direction][0], 
                            edge_tiles[tile][1] + ind * OFFSETS[direction][1]))
            # gathering tile values of the line 
            for ind in indices:
                line.append(self.get_tile(ind[0], ind[1]))
            # sliding and merging values of the extracted line
            merged_line = merge(line)
            # reflecting the new merged line on to the grid
            for tile in range(len(merged_line)):
                self.set_tile(indices[tile][0], indices[tile][1], merged_line[tile])
        # adds new tile if there was a change in the grid
        if prior_grid != str(self):
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        empty_tile_indexes = []
        # finding indexes of all empty tiles
        for row in range(self.get_grid_height()):
            for col in range(self.get_grid_width()):
                if self._grid[row][col] == 0: 
                    empty_tile_indexes.append((row, col))
        # selecting one of the empty tile indexes at random            
        rand_tile_index = random.choice(empty_tile_indexes)
        # chosing value for random tile
        if random.random() < 0.9:
            rand_tile_val = 2
        else:
            rand_tile_val = 4
        self.set_tile(rand_tile_index[0], rand_tile_index[1], rand_tile_val)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # setting value of chosen random empty tile
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]

def test_suite():    
    """
    Test suite to run tests on the TwentyFortyEight class and functions
    """
    test_game = TwentyFortyEight(4, 4)
    print test_game
    print test_game.get_tile(0, 2)
    test_game.new_tile()
    test_game.new_tile()
    test_game.new_tile()
    test_game.new_tile()
    test_game.set_tile(3, 3, 69)
    print test_game
    test_game.move(UP)
    print test_game
    
    print merge([2, 0, 2, 4])
    print merge([0, 0, 2, 2])
    print merge([2, 2, 0, 0])
    print merge([2, 2, 2, 2, 2])
    print merge([8, 16, 16, 8])
    print merge([8, 0, 0, 8])
        
#test_suite()
        
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
