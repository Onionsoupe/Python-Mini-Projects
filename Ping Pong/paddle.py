from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.setheading(90)
        self.goto(position, 0)
        self.speed("fastest")

    def paddle_up(self):
        if self.ycor() < 250:
            self.setheading(90)
            self.forward(20)

    def paddle_down(self):
        if self.ycor() > -250:
            self.setheading(270)
            self.forward(20)