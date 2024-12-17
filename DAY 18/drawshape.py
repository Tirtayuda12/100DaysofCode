from turtle import Turtle
Tirta = Turtle()
def shape(segi):
    derajat_bangun = 360/segi
    Tirta.pencolor("red")
    Tirta.fillcolor("yellow")
    for _ in range(segi):
        Tirta.forward(100)
        Tirta.left(derajat_bangun)

segi = int(input("Segi berapa yang ingin anda gambarkan: "))


shape(segi)