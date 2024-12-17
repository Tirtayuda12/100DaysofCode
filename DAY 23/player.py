STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_turtle()

    
    def create_turtle(self):
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(0,-280)
    
    def move(self):
        new_y = self.ycor() + 10
        self.goto(0,new_y)
    
    def reset_player(self):
        self.goto(0,-280)

    
    


