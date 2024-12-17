from turtle import Turtle, Screen


tirta = Turtle()
screen = Screen()

# w key
def move_foward():
    tirta.forward(10)

# s key
def move_backward():
    tirta.back(10)

# d key
def move_clockwise():
    tirta.right(10)
# a key
def move_Counterclockwisse():
    tirta.left(10)

def clear_screen():
    tirta.penup()
    tirta.clear()
    tirta.home()
    tirta.pendown()

screen.onkey(key="w",fun=move_foward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d",fun=move_clockwise)
screen.onkey(key="a",fun=move_Counterclockwisse)
screen.onkey(key="c",fun=clear_screen)
screen.listen()
screen.exitonclick()
