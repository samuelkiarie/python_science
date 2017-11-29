class cardsplay(object):
    def __init__(self):
        self.deck = []
        self.values =[]
        self.value = []

    def cards(self):
        suits = ['diamond','hearts','clubs','spade']
        for rank  in range(2, 5):
            if rank == 11:
                value = 'jack'
            if rank == 12:
                value = 'queen'
            if rank == 13:
                value = 'king'
            if rank == 14:
                value = 'ace'
            else:
                value = str(rank)
            self.values.append(self.value)
        complete_deck = [(val, suit)for val in self.values for suit in suits]
        self.deck.append(complete_deck)
        print self.deck

