import random
import os
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

yes_no = ["yes", "no"]

def deal_card(who: list):
    """Puts card in designated list."""
    cards = [11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    who.append(card)

def hit(who):
    """Deal card to player."""
    deal_card(who)

def stand():
    """Player doesnt want card; so dealer doesnt deal."""
    pass

def check_ace(hand):
    """If hand has ace and total is more than 21 ace is made a 1."""
    count = 0
    for ace in hand:
        if ace == 11 and sum(hand) > 21:
            hand[count] = 1
        count += 1


dealer_hand = [11, 11]

player_hand = [10, 5]

print(dealer_hand)
check_ace(dealer_hand)
print(dealer_hand)

#play = input("Would you like to play BlackJack?[yes/no]\n").lower()
#if play not in yes_no:
#    print("Invalid input, try again.")
#    play = input("Would you like to play BlackJack?[yes/no]\n").lower()
