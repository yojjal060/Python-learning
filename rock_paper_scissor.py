import random



choice = int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))



random = int(random.randint(0, 3))
if random == 0:
    print("Computer chose rock")
    if choice == 0:
        print("It's a tie. Try again.")
    elif choice == 1:
        print("Yow won!!")
    elif choice == 2:
        print("You lose!!")

elif random == 1:
    print("Computer chose paper")
    if choice == 0:
        print("You lose!!")
    elif choice == 1:
        print("It's a tie. Try again.")
    elif choice == 2:
        print("You lose!!")
elif random == 2:
    print("computer chose scissors.")
    if choice == 0:
        print("You lose!!")
    elif choice == 1:
        print("You won!!")
    elif choice == 2:
        print("It's a tie. Try again!!")
