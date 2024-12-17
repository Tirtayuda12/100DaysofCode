from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500,height=400)
turtle1 = Turtle(shape='turtle')
turtle2 = Turtle(shape='turtle')
turtle3 = Turtle(shape='turtle')
turtle4 = Turtle(shape='turtle')
turtle5 = Turtle(shape='turtle')
turtle6 = Turtle(shape='turtle')
turtles = [turtle1,turtle2,turtle3,turtle4,turtle5,turtle6]
colors = ['blue','green','yellow','orange','red','magenta']
i=0
y=0
for turtle in turtles:
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x =-220,y=y + -100)
    y=y+40
    i+=1

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 220:
            is_race_on=False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} winning")
            else:
                print(f"You've lost! the {winning_color} winning")
        rand_distance=random.randint(1,10)
        turtle.forward(rand_distance)
    


    



screen.exitonclick()