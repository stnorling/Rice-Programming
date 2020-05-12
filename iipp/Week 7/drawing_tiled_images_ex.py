# demo for drawing using tiled images

import simplegui

# define globals for cards
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
SUITS = ('C', 'S', 'H', 'D')

# card sprite - 950x392
CARD_CENTER = (36.5, 49)
CARD_SIZE = (73, 98)
card_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")



# define card class
class Card:
    def __init__(self, suit, rank):
        self.rank = rank
        self.suit = suit

    def draw(self, canvas, loc):
        # Below finds index of the rank argument (e.g. A, 5, 8, Q, K, etc.) in our RANKS list.
        i = RANKS.index(self.rank)
        # Below finds the index of the suit argument ('C', 'S', etc.) in our SUITS list.
        j = SUITS.index(self.suit)
        # card_pos is the center of the card provided in the argument when we created the Card object.
        # it works by moving across the tiled image to locate the given card as per the index values of the rank and suit.
        # it moves between cards by distance of card width (for rank, laterally) and card height (for suit, vertically).
        card_pos = [CARD_CENTER[0] + i * CARD_SIZE[0],
                    CARD_CENTER[1] + j * CARD_SIZE[1]]
        # the image is then drawn at argued location 'loc'. 
        canvas.draw_image(card_image, card_pos, CARD_SIZE, loc, CARD_SIZE)

# define draw handler        
def draw(canvas):
    one_card.draw(canvas, (155, 90))

# define frame and register draw handler
frame = simplegui.create_frame("Card draw", 300, 200)
frame.set_draw_handler(draw)

# createa Card object
one_card = Card('S', '6')

frame.start()
