from turtle import Turtle,Screen

timmy = Turtle()
print(timmy)

def movement():
    timmy.shape("turtle")
    timmy.color("coral")
    timmy.forward(100)
    timmy.left(120)
    timmy.forward(100)
    timmy.left(120)
    timmy.forward(100)

movement()

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
