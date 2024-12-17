# turtle event listener
from turtle import Turtle, Screen

tirta = Turtle()
screen = Screen()


def move_foward():
    tirta.forward(10)

def move_left():
    tirta.left(90)

def move_right():
    tirta.right(90)


screen.onkey(key="space",fun=move_foward)
screen.onkey(key="Right", fun=move_right)
screen.onkey(key="Left",fun=move_left)
screen.listen()
screen.exitonclick()