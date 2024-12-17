import turtle as t
import math
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
Tirta.pensize(15)
for _ in range(100):
    Tirta.color(random_color())
    directions = math.ceil(math.degrees((random.randint(0,4)*math.pi)/2))
    Tirta.forward(25)
    Tirta.left(directions)
    