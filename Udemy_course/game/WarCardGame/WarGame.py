from PythonCourse import Player, Deck

player_one = Player("One")
player_two = Player("Two")
new_deck = Deck()
new_deck.shuffle()

for i in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_count = 0
while game_on:
    round_count+=1
    print("Round {0}".format(round_count))
    if len(player_one.all_cards) == 0:
        print("Player one is out of card! Player two wins!")
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print("Player two is out of card! Player one wins!")
        game_on = False
        break

    #start new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    print(player_one_cards[-1])
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    print(player_two_cards[-1])
    at_war = True
    if player_one_cards[-1].value > player_two_cards[-1].value:
        at_war = False
        player_one.add_cards(player_one_cards)
        player_one.add_cards(player_two_cards)
        print("Player One takes cards")
    elif player_one_cards[-1].value < player_two_cards[-1].value:
        at_war = False
        player_two.add_cards(player_one_cards)
        player_two.add_cards(player_two_cards)
        print("Player Two takes cards")
    else:
        print("War!")
        if len(player_one.all_cards) < 5:
            print("Player One is unable to declare war!")
            print("Player Two wins!")
            game_on = False
            break
        elif len(player_two.all_cards) < 5:
            print("Player Two is unable to declare war!")
            print("Player One wins!")
            game_on = False
            break
        else:
            for i in range(5):
                player_one_cards.append(player_one.remove_one())
                player_two_cards.append(player_two.remove_one())