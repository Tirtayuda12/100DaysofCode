from turtle import Turtle
import math
import random

colors = ["teal","aquamarine","turquoise","lime","olive","khaki","dark goldenrod","saddle brown","firebrick","maroon","deep pink","crimson","medium violet red","purple","dark slate blue"]
Tirta = Turtle()
Tirta.speed("fast")
Tirta.pensize(15)
for _ in range(200):
    Tirta.color(random.choice(colors))
    directions = math.ceil(math.degrees((random.randint(0,4)*math.pi)/2))
    Tirta.forward(25)
    Tirta.left(directions)
    