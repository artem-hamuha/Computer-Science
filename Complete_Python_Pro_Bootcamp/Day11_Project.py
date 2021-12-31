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
    deal_card(who)

def total(hand):
    sum = 0
    for num in hand:
        sum += num

dealer_hand = []
dealer_total = total(dealer_hand)

player_hand = []
player_total = total(player_hand)

play = input("Would you like to play BlackJack?[yes/no]\n").lower()
if play not in yes_no:
    print("Invalid input, try again.")
    play = input("Would you like to play BlackJack?[yes/no]\n").lower()


while play == "yes":
    while len(dealer_hand) is not 2 and len(player_hand) is not 2:
        deal_card(player_hand)
        deal_card(dealer_hand)

