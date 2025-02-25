import turtle
import colorgram
import random
from turtle import Turtle, Screen
colors = colorgram.extract('image.jpg', 25)
color_list=[ (202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19)]
turtle.colormode(255)
tim = Turtle()
tim.pensize(20)
tim.penup()
y = 225
tim.setposition(-225,-y)
for n in range(10):
    for i in range(10):
        tim.pendown()
        tim.pencolor(random.choice(color_list))
        tim.forward(1)
        tim.penup()
        tim.forward(50)
        tim.pendown()
    tim.penup()
    y = y-50
    tim.setposition(-225, -y)
print(color_list)
screen = Screen()
screen.exitonclick()

