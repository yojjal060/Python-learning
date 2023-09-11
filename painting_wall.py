import math

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
number_of_cans = math.ceil(test_h*test_w/coverage)

print(f"You'll need {number_of_cans} number of cans")
