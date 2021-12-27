import os
#HINT: You can call clear() to clear the output in the console.

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bidders = {}

print(logo)
print("Welcome to the biidding simulator\n")

l = 1
run = True
while run == True:
    name = input("Name of bidder - ")
    amount = int(input("Amount biidding - "))

    bidders[name] = amount

    yes_no = input("Any other bidders [yes/no] - ").lower()

    if yes_no == "yes":
        os.system("cls")
    else:
        highest_bid = 0
        winner = ""
        for b in bidders:
            bid_amount = bidders[b]
            if bid_amount > highest_bid: 
                highest_bid = bid_amount
                winner = b
        print(f"The winner is {winner} with a bid of ${highest_bid}")
        run = False
