from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, coordinate):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(coordinate, 220)

    def update_scoreboard(self):
        self.write(arg=self.score, align="left", font=("Courier", 60, "bold"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align="Center", font=("Courier", 28, "normal"))