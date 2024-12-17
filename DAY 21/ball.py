from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    
    def move_ball(self):
        x_pos = self.xcor()+ self.x_move
        y_pos = self.ycor()+ self.y_move
        self.goto(x_pos,y_pos)
    
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()
        
        # if x_pos >= 400 or x_pos<= -300:
        #     print("You loose!!")
        #     return 
        # elif 
    
