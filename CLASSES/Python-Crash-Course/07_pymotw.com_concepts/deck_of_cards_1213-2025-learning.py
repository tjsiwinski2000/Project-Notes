#https://pymotw.com/3/random/index.html 
#A simulation of a card game needs to mix up the deck of cards and then deal them to the players, without using the same card more than once. Using choice() could result in the same card being dealt twice, so instead, the deck can be mixed up with shuffle() and then individual cards removed as they are dealt.

# 1213-2025 - TJS trying to write show deck 
import random
import itertools

FACE_CARDS = ('J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'C', 'S')


def new_deck():
    return [
        # Always use 2 places for the value, so the strings
        # are a consistent width.
        '{:>2}{}'.format(*c)
        for c in itertools.product(
            itertools.chain(range(2, 11), FACE_CARDS),
            SUITS,
        )
    ]


def show_deck(deck):
    p_deck = deck[:]
    while p_deck:
        row = p_deck[:13]
        p_deck = p_deck[13:]
        for j in row:
            print(j, end=' ')
        print()

def show_deck_tj(deck):
    line = ""
    for count in range (1,len(deck)):
        line += " " + deck[count]
        if count %13 ==0:
            print(line)
            line = ""
        
# Make a new deck, with the cards in order
deck = new_deck()
print('Initial deck:')
show_deck(deck)
print('Initial deck-TJ:')
show_deck_tj(deck)

# Shuffle the deck to randomize the order
random.shuffle(deck)
print('\nShuffled deck:')
show_deck(deck)

# Deal 4 hands of 5 cards each
hands = [[], [], [], []]

for i in range(5):
    for h in hands:
        h.append(deck.pop())

# Show the hands
print('\nHands:')
for n, h in enumerate(hands):
    print('{}:'.format(n + 1), end=' ')
    for c in h:
        print(c, end=' ')
    print()

# Show the remaining deck
print('\nRemaining deck:')
show_deck(deck)