# implementing a simple snake game using the turtle module in Python.

import turtle
import time
import random
from snake_gui import setup_screen, update_screen
from snake_objects import head, food, segments, score_display, reset_game
from snake_controls import go_up, go_down, go_left, go_right, move

delay = 0.1
score = 0
high_score = 0

# GUI Setup
wn = setup_screen()

# Keybinding
wn.listen()
wn.onkey(lambda: go_up(head), "w")
wn.onkey(lambda: go_down(head), "s")
wn.onkey(lambda: go_left(head), "a")
wn.onkey(lambda: go_right(head), "d")

# Main loop
while True:
    wn.update()
    update_screen(head, segments)
    move(head, wn)

    # Gameplay
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        score += 1

        if score > high_score:
            high_score = score

        score_display.clear()
        score_display.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    for segment in segments[1:]:
        if head.distance(segment) < 20:
            reset_game() 

    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        reset_game()

    time.sleep(delay)
