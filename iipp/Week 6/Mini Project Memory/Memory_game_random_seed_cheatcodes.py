# Function that finds a number of seed arguments to
# random.seed() that return 5 or more pairs of numbers in a
# row. The aim is to find seed numbers that allow 
# completion of the Memory game in the least number of turns.

def pairs(deck):
    count = 0
    for i in range(15):
        if deck[i] == deck[i+1]:
            count += 1
    return count > 4
        
import random
unicorns = []

# We run 800 iterations at a time below, but more can be done.

while len(unicorns) < 1:

    for i in range(800):
        
        secret_number = random.randrange(0,999999)
        random.seed(secret_number)
        #print('xx:',secret_number)

        # build deck 
        deck = [card for card in range(8)  for trip in range(2)]
        random.shuffle(deck)
        #print(deck)
        if pairs(deck):
            unicorns.append(secret_number)

print("UNICORNS",unicorns)