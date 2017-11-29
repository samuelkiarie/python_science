def deck_cards(suits, rank):
    return [(suit, ranks)for suit in suits for rank in ranks]
suits = ['spades','hearts','flowers','diamonds']
rank = range(1,14)
    print(suits,rank)
