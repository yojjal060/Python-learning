import guessthenumber_art
import random

guessthenumber_art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

#function check answer
def check_answer(guess,answer,turns):
    if guess>answer:
        print("Too high")
        return turns -1
    elif guess < answer:
        print("Too low.")
        return turns -1
    else:
        print(f"You got it! The answer was {answer}.")


#function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard' : ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the Number Guessing Game!!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    print(f"pssst , the correct answer is {answer}")


    turns = set_difficulty()

    

    guess=0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a Guess: "))
        turns = check_answer(guess, answer,turns)
        if turns == 0:
            print("You are run out of guesses, you lose. ")
            return
game()