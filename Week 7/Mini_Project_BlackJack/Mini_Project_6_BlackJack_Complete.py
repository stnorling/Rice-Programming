# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        # card_loc finds the center of the given card we want to display
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        hand_str = ""
        for c in self.cards:
            hand_str += str(c) + " "
        return 'hand contains ' + hand_str
            
    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        hand_value = 0
        ace = False
        for c in self.cards:
            hand_value += VALUES[c.get_rank()]
            if c.get_rank() == 'A':
                ace = True
        if ace == True and hand_value < 12:
            hand_value += 10
        return hand_value
   
    def draw(self, canvas, pos):
        if self.cards:
            for i in range(len(self.cards)):
                self.cards[i].draw(canvas, [pos[0] + (i * CARD_SIZE[0] * 1.25), pos[1]])
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = [Card(i, j) for i in SUITS for j in RANKS]
        random.shuffle(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
    
    def __str__(self):
        deck_str = ""
        for c in self.deck:
            deck_str += str(c) + " "
        return 'Deck contains ' + deck_str


#define event handlers for buttons
def deal():
    global outcome, in_play, deck, dealer_hand, player_hand, score
    
    if in_play:
        score -= 1
        outcome = 'Dealt during round. Player loses. Hit or stand?'
    else:
        outcome = 'Hit or stand?'

    dealer_hand = Hand()
    player_hand = Hand()
    deck = Deck()

    deck.shuffle()

    for i in range(2):
        dealer_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())

        #print 'Dealer ' + str(dealer_hand)
        #print 'Player ' + str(player_hand)
        #print player_hand.get_value()

        in_play = True
        

def hit():
    global score, in_play, outcome
    
    if in_play:
        if player_hand.get_value() < 21:
            player_hand.add_card(deck.deal_card())
            #print 'Player ' + str(player_hand)
            #print player_hand.get_value()
            if player_hand.get_value() > 21:
                outcome = 'Player busts.'
                score -= 1
                in_play = False
    else:
        outcome = 'Game is not in play. New deal?'
        
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global dealer_hand, score, in_play, outcome
    
    if in_play:
        in_play = False        
        #print 'Dealer hand value: ', dealer_hand.get_value()
        
        while dealer_hand.get_value() < 17:
            
            dealer_hand.add_card(deck.deal_card())
            #print 'Dealer hits. Hand value: ', dealer_hand.get_value()
            #print 'Dealer ' + str(dealer_hand)
            
        if dealer_hand.get_value() > 21:
            outcome = 'Dealer busts. Player wins. New deal?'
            score += 1
        elif player_hand.get_value() > dealer_hand.get_value():
            outcome = 'Player wins. New deal?'
            score +=1
        elif player_hand.get_value() == dealer_hand.get_value():
            outcome = 'Dealer wins. House wins on ties. New deal?'
            score -= 1
        else:
            outcome = 'Dealer wins. New deal?'
            score -= 1
    
    else:
        outcome = 'Game is not in play. New deal?'

# draw handler    
def draw(canvas):
    
    dealer_hand.draw(canvas, [80, 250])
    player_hand.draw(canvas, [80, 380])
    
    canvas.draw_text('Blackjack', [80, 80], 44, 'Black')
    canvas.draw_text('Score: ' + str(score), [440, 80], 24, 'Black')
    canvas.draw_text(outcome, [80, 200], 24, 'Black')
    
    if in_play:
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * 1, 
                    CARD_CENTER[1] + CARD_SIZE[1] * 0)
        canvas.draw_image(card_back, card_loc, CARD_SIZE, [80 + CARD_CENTER[0], 250 + CARD_CENTER[1]], CARD_SIZE)
        

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

# remember to review the gradic rubric