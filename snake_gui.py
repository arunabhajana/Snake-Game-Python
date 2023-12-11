
"""
    The code defines a function that updates the screen by moving the segments of a snake game.
    :return: The `setup_screen` function returns the turtle screen object (`wn`).
"""
import turtle

def setup_screen():
    wn = turtle.Screen()
    wn.title("Snake Game")
    wn.bgcolor("black")
    wn.setup(width=600, height=600)
    wn.tracer(0)
    return wn

def update_screen(head, segments):
    move_segments(head, segments)

def move_segments(head, segments):
    for index in range(len(segments)):
        if index == 0:
            x = head.xcor()
            y = head.ycor()
        else:
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()

        segments[index].goto(x, y)

    turtle.update()
