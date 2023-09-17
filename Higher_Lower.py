from high_low_art import logo,vs
from high_low_data import data
import random
import os

#format the account data into printable format.
def format_data(account):
    """" fomat the account data into printable format. """
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return (f"{account_name}, a {account_descr}, from {account_country}")

def check_answer(guess, a_followers,b_followers):
    """"Take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        if guess == "a":
            return True
    else:
        if guess == "b":
            return True



#display art
print(logo)
score = 0

game_should_continue = True
account_b = random.choice(data)

while game_should_continue:
    #import data from existing py file
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}." )


    #Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B' : ").lower()




    #check if user is correct.
    ##Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    ##Use if statement to check if user is correct.

    is_correct = check_answer(guess, a_follower_count,b_follower_count )


    #Give user feedback on their guess.
    os.system('cls')
    print(logo)
    #score keeping.
    if is_correct:
        score += 1
        print(f"You'r right! Current score : {score}.")
        
    else:
        game_should_continue = False
        print(f"sorry that's wrong!!. Final score: {score}")
    

#Making accounts at position B become the next account at Position A.

#clear the screen.




