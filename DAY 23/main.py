import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.move,"Up")

game_is_on = True
car_speed = 0.1
while game_is_on:
    time.sleep(car_speed)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
    
    if player.ycor() > 250:
        player.reset_player()
        scoreboard.level += 1
        scoreboard.update_scoreboard()
        car_speed *= 0.9

        




screen.exitonclick()