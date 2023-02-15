from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=400)
# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "brown", "green", "violet"]

x = -280
y = -135

for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=x, y=y)
    y += 50

screen.exitonclick()
