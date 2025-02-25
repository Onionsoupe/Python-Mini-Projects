from turtle import Turtle, Screen
import time
from car_manager import CarManager
from scoreboard import Scoreboard
from player import Player
import random

timer=0.2
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager()
car_choice = [True, False]

player = Player()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.player_move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(timer)
    screen.update()
    if random.choice(car_choice):
        car.car_generator()
    for i in range(len(car.cars)):
        car.move_car(i)
        if player.distance(car.cars[i]) < 30:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() == 280:
        player.player_reset()
        scoreboard.score +=1
        scoreboard.clear()
        scoreboard.point_increase()
        timer = timer-0.01


screen.exitonclick()


