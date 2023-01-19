from turtle import Turtle, Screen
from random import randint

tim = Turtle()
# tim.shape("arrow")
tim.color("dark magenta")

# for _ in range(10):
#     tim.forward(4)
#     tim.penup()
#     tim.forward(4)
#     tim.pendown()

for _ in range(4):
    tim.forward(100)
    tim.right(90)

for _ in range(5):
    tim.forward(100)
    tim.right(72)

for _ in range(6):
    tim.forward(100)
    tim.right(360/6)

for _ in range(7):
    tim.forward(100)
    tim.right(360/7)

for _ in range(8):
    tim.forward(100)
    tim.right(360/8)










screen = Screen()
screen.exitonclick()

