import turtle as t
import random


Tirta = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colors = (r,g,b)
    return colors

Tirta.speed("fast")
Tirta.pensize(1)
for _ in range(100):
    Tirta.color(random_color())
    Tirta.circle(50)
    current_heading = Tirta.heading()
    Tirta.setheading(current_heading+10)
    Tirta.circle(50)
