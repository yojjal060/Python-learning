print("!!!Welcome To Treasure Island!!!\n!!!Your mission is to find the treasure.!!!")
cross_road = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'.")
if cross_road == 'left':
    lake = input("You come to a lake. There is an island in the middle of the lake. Type 'wait'to wait for a boat. Type 'swim' to swim across. ")
    if lake == 'wait':
        color = input("You arrive at the island unharmed. There is house with 3 doors. One red, one yellow and one blue. Which color do you choose?")
        if color == 'blue':
            print("you enter a room of beasts. Game OVER")
        elif color == 'yellow':
            print("!!!YAYYYY. You found the treasuree!!!")
        elif color == 'red':
            print("get blowjobed by two gay men. Game Over")
    elif lake == 'swim':
        print("Wasted.\ndeep throated by shark.")
else:
    print("oooops. You fell into a hole. !!Game Over!!")