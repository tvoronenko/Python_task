class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            #multiple cards objects
            self.all_cards.extend(new_cards)
        else:
            #single card
            self.all_cards.append(new_cards)

    def __str__(self):
        return "Player {0} has {1} cards".format(self.name, len(self.all_cards))