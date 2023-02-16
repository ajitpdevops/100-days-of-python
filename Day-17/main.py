from turtle import Screen, Turtle
from random import randint
import time

screen = Screen()
colors = ['Red', 'Orange', 'Yellow', 'Blue', 'Green', 'Indigo', 'Violet']
screen.setup(height=600, width=800)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

game_on = True

x = -340
y = -190

turtles = []

for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=x, y=y)
    y += 70
    turtles.append(new_turtle)

time.sleep(3)

while game_on:
    for turtle_index in range(len(turtles)):
        turtles[turtle_index].forward(randint(0, 10))
        pos = turtles[turtle_index].pos()
        if pos[0] >= 340:
            winner = colors[turtle_index]
            game_on = False

if user_bet == winner:
    print(f'You win, your {user_bet} turtle won the race.')
else:
    print(f'You lose, the race winner is - {winner}')

screen.exitonclick()

