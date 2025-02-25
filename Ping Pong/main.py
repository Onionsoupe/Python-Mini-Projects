from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

r_paddle = Paddle(360)
l_paddle = Paddle(-360)
ball = Ball()
scoreboard_l = Scoreboard(-50)
scoreboard_r = Scoreboard(50)

screen.listen()
screen.onkeypress(r_paddle.paddle_up, "Up")
screen.onkeypress(r_paddle.paddle_down, "Down")
screen.onkeypress(l_paddle.paddle_up, "w")
screen.onkeypress(l_paddle.paddle_down, "s")

is_game_on = True

while is_game_on:
    time.sleep(0.06)
    scoreboard_l.clear()
    scoreboard_r.clear()
    scoreboard_l.update_scoreboard()
    scoreboard_r.update_scoreboard()
    screen.update()
    ball.move()
    if ball.ycor() > 287 or ball.ycor() < -287:
        ball.bounce_y()
    elif ball.xcor() > 387:
        ball.goto(0,0)
        scoreboard_l.score += 1
        ball.bounce_x()
    elif ball.xcor() < -387:
        ball.goto(0, 0)
        scoreboard_r.score += 1
        ball.bounce_x()

    if ball.distance(r_paddle)  < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()




screen.exitonclick()