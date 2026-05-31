import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

ball = Ball()
scoreboard = Scoreboard()

p1 = Paddle((370,0))
p2 = Paddle((-370,0))

screen.onkeypress(p1.up, "Up")
screen.onkeypress(p2.up, "w")
screen.onkeypress(p1.down, "Down")
screen.onkeypress(p2.down, "s")



game_is_on = True


while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 350 and ball.distance(p1) < 50 or ball.xcor() < -350 and ball.distance(p2) < 50:
        ball.bounce_x()

    if ball.xcor() > 380:
        time.sleep(0.5)
        scoreboard.l_point()
        scoreboard.update_scoreboard()
        ball.reset_ball()

    if ball.xcor() < -380:
        time.sleep(0.5)
        scoreboard.r_point()
        scoreboard.update_scoreboard()
        ball.reset_ball()

screen.exitonclick()
