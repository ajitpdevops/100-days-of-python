import turtle
import colorgram
import turtle as turtle_module
import random

# Export the colors from the image using colorgram
# colors = colorgram.extract('image.jpg', 12)

# color_list = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
#
# print(color_list)

color_list = [(212, 154, 98), (53, 107, 132), (174, 78, 36), (199, 142, 34), (117, 155, 171), (125, 79, 98), (123, 175, 157), (227, 198, 129)]
tim = turtle_module.Turtle()
turtle.colormode(255)

tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(210)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_number in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    tim.dot(20, random.choice(color_list))

    if dot_number % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




#TODO
# 1. Turn Right move 50 spaces
# 2. Turn Left move 10 spaces
# 3. Turn Left and move 50 spaces
# 4. Turn Right and move 10 spaces
# 5. Turn Right and move 50 spaces

# def move_forward():
#
#     for _ in range(11):
#         tim.forward(10)
#         tim.penup()
#         tim.forward(10)
#         tim.pencolor(random.choice(color_list))
#         tim.pendown()
#
#
# for _ in range(5):
#     move_forward()
#     tim.left(90)
#     tim.penup()
#     tim.forward(30)
#     tim.left(90)
#     tim.pendown()
#     move_forward()
#     tim.right(90)
#     tim.penup()
#     tim.forward(30)
#     tim.right(90)
#     tim.pendown()


screen = turtle_module.Screen()
screen.exitonclick()
