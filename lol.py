print("welcome to rollercoaster")
height = int(input("What is your height? "))

if height>=120:
    print("You can ride")
    age = int(input("What is your age? "))
    if age>18:
        
        print("The total cost of ride is $12")
    elif age<12:
        print("The total cost of ride is $5")
    else:
        print("The total cost of ride is $7")
else:
    print("You can't ride")