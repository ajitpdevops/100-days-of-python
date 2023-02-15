from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# Etch a Sketch Program
# TODO: 1. W:Forwards
# TODO: 2. S:Backwards
# TODO: 3. A=Counter-Clockwise
# TODO: 4. B=Clockwise
# TODO: 5. C=ClearDrawing


def move_forwards():
    tim.setheading(0)
    tim.forward(10)


def move_backwards():
    tim.setheading(180)
    tim.forward(10)


def turn_counter_clockwise():
    tim.left(10)
    tim.forward(10)


def turn_clockwise():
    tim.right(10)
    tim.forward(10)


def clear_drawing():
    tim.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear_drawing)

screen.exitonclick()
