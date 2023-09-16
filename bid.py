import os
bids = {}

bidding_finished = False

while not bidding_finished:
    os.system('cls')
    name = input("What is your name?")
    price = input("What is your bid? $")
    bids[name] = price
    should_countinue = input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_countinue == "no":
        bidding_finished = True
    
        
