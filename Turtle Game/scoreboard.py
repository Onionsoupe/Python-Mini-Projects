from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.game_status = None
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-255, -285)
        self.write(f"Score = {self.score} ", align="center", font=("Courier",10, "normal"))


    def point_increase(self):
        self.write(f"Score = {self.score} ", align="center", font=("Courier",10, "normal"))
        
    def game_over(self):
        self.game_status = Turtle()
        self.game_status.hideturtle()
        self.game_status.penup()
        self.game_status.write("Game over", align="center", font=FONT)
        