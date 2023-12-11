"""
    The code defines a function called `reset_game()` that resets the snake game by moving the
    snake's head and segments to their initial positions, clearing the segments, resetting the score,
    and updating the score display.
"""
import turtle

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Right"

food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)


global high_score
high_score = 0

def reset_game():
    
    head.goto(0, 0)
    head.direction = "Right"

    
    for segment in segments:
        segment.goto(1000, 1000)  #
    segments.clear()

    global score
    score = 0

    score_display.clear()
    score_display.write("Score: 0  High Score: {}".format(high_score), align="center", font=("Courier", 24, "normal"))
