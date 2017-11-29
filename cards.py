from random import *
def deck_cards():
    values = []
    value = []
    for rank in range(2, 15):
            if rank == 11:
                value = 'jack'
            elif rank == 12:
                value = 'queen'
            elif rank == 13:
                value = 'king'
            elif rank == 14:
                value = 'ace'
            else:
                value =str(rank)
            values.append(value)
    suits = ['spades','diamonds','clubs', 'hearts']
   # x = len(rank)*len(suits)
    cards = [(val , suit) for val in values for suit in suits]
    return cards
     

deck_cards()



















