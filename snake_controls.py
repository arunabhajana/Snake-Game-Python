"""
    The code defines functions to move an object up, down, left, or right, and a function to move
    the object based on its current direction.
    
    :param head: The parameter "head" represents the head of a snake in a game. It is an object that has
    attributes such as direction, xcor, and ycor. The direction attribute represents the current
    direction the snake is moving in (up, down, left, or right). The xcor and y
"""
def go_up(head):
    if head.direction != "down":
        head.direction = "up"

def go_down(head):
    if head.direction != "up":
        head.direction = "down"

def go_left(head):
    if head.direction != "right":
        head.direction = "left"

def go_right(head):
    if head.direction != "left":
        head.direction = "right"

def move(head, wn):
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    wn.update()
