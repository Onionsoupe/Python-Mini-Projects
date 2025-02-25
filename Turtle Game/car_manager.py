from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()

    def car_generator(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(1,2)
        new_car.penup()
        new_car.goto(300, random.randint(-200, 300))
        new_car.setheading(180)
        self.cars.append(new_car)

    def move_car(self,index):
        self.cars[index].forward(MOVE_INCREMENT)
