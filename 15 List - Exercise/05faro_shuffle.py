initial_deck = input().split()
shuffles = int(input())

for shuffle in range(shuffles):
    deck_middle = int(len(initial_deck) / 2)
    left_cards = initial_deck[:deck_middle]
    right_cards = initial_deck[deck_middle:]

    current_deck = []
    for card_index in range(len(left_cards)):
        current_deck.append(left_cards[card_index])
        current_deck.append(right_cards[card_index])
    initial_deck = current_deck

print(initial_deck)



#################################### TASK CONDITION ############################
"""
                           5.	Faro Shuffle
A faro shuffle is a method for shuffling a deck of cards, in which the deck is split
exactly in half. Then the cards in the two halves are perfectly interleaved, 
such that the original bottom card is still on the bottom and the original top card is still on top.
For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once,
gives ['ace', 'four', 'two', 'five', 'three', 'six']
Write a program that receives a single string (cards separated by space)
and on the second line receives a count of faro shuffles that should be made.
Print the state of the deck after the shuffle.
Note: The length of the deck of cards will always be an even number.


____________________________________________________________________________________________
Example_01

Input
a b c d e f g h
5

Output
['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']


____________________________________________________________________________________________
Example_02

Input
one two three four
3

Output
['one', 'three', 'two', 'four']

"""
