from tkinter.constants import CENTER
from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("savescore.txt", mode='r') as file:
            r = int(file.read())
        self.highscore = r
        self.color("white")
        self.penup()
        self.goto(-280, -280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score = {self.score} Highscore = {self.highscore}", align="left", font=("Courier", 10, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("savescore.txt", mode='w') as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER!", align="Center", font=("Courier", 28, "normal"))

    def score_update(self):
        self.clear()
        self.score +=1
        self.update_scoreboard()

