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
    """For dealing cards in the begining of the game."""
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





print(logo)

play = input("Would you like to play BlackJack? [yes/no]\n").lower()
while play not in yes_no:
    print("Invalid input, try again.")
    play = input("Would you like to play BlackJack? [yes/no]\n").lower()

while play == "yes":
    player_hand = []

    dealer_hand = []

    while len(player_hand) != 2 and len(dealer_hand) != 2:
        deal_card(player_hand)
        deal_card(dealer_hand)

    dealer_hand_1c = ["?", dealer_hand[1]]
    
    print(f"\nYour Hand: {player_hand}\nTotal: {sum(player_hand)}")
    print(f"\nDealer Hand: {dealer_hand_1c}\nTotal: {dealer_hand[1]}")

    if sum(player_hand) == 21:
        print("\nBlackJack!!!\nYou Win!")
        break

    hit_stand = input("Would you like to hit [yes/no]\n").lower()

    while hit_stand not in yes_no:
        print("\nInvalid input, try again.")
        hit_stand = input("Would you like to hit [yes/no]\n").lower()
    
    while hit_stand == "yes":
        check_ace(player_hand)
        hit(player_hand)
        check_ace(player_hand)

        if sum(player_hand) > 21:
            print(f"\nYour Hand: {player_hand}\nTotal: {sum(player_hand)}")
            print("\nYou Bust.\nDealer Wins!")
            break

        print(f"\nYour Hand: {player_hand}\nTotal: {sum(player_hand)}")
        print(f"\nDealer Hand: {dealer_hand}\nTotal: {sum(player_hand)}")
        hit_stand = input("\nWould you like to hit [yes/no]\n").lower()
        while hit_stand not in yes_no:
            print("\nInvalid input, try again.")
            hit_stand = input("\nWould you like to hit [yes/no]\n").lower()
    
    print(f"Dealer Hand: {dealer_hand}\nTotal: {sum(dealer_hand)}")

    while sum(dealer_hand) < 17:
        check_ace(dealer_hand)
        hit(dealer_hand)
        check_ace(dealer_hand)

        if sum(dealer_hand) > 21:
            print(f"Dealer Hand: {dealer_hand}\nTotal: {sum(dealer_hand)}")
            print("Dealer Busts.\nPlayer Wins!")
            break
        
        print(f"\nDealer Hand: {dealer_hand}\nTotal: {sum(dealer_hand)}")
    
    if dealer_hand < player_hand:
        print("Player Wins!")
    
    elif dealer_hand > player_hand:
        print("Dealer Wins!")
    
    else:
        print("Push.")
    
    play = input("\nWould you like to play again? [yes/no]\n").lower()
    while play not in yes_no:
        print("\nInvalid input, try again.")
        play = input("Would you like to play BlackJack? [yes/no]\n").lower()