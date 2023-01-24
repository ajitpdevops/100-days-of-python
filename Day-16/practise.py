import turtle
from turtle import Turtle, Screen
from random import randint, choice
import turtle as t
tim = Turtle()
colors = ["wheat", "gold", "dark red", "olive drab", "dark magenta", "dark cyan", "purple", "turquoise", "green", "lime", "gray"]
directions = [0, 90, 180, 270]
# tim.shape("arrow")
# tim.color("dark magenta")

# # Draw a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# # Draw a dotted line
# for _ in range(10):
#     tim.forward(4)
#     tim.penup()
#     tim.forward(4)
#     tim.pendown()


# # Draw shapes
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for num in range(3, 11):
#     tim.pencolor(choice(color))
#     draw_shape(num)


tim.hideturtle()
# tim.width(10)
tim.speed("fastest")
turtle.colormode(255)


# generate a random a color
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


# for _ in range(200):
#     tim.pencolor(random_color())
#     tim.forward(25)
#     tim.setheading(choice(directions))
tilt_angle = 5
for _ in range(0, int(360/tilt_angle)):
    tim.pencolor(random_color())
    tim.circle(100)
    tim.right(tilt_angle)






screen = Screen()
screen.exitonclick()

