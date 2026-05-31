from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.y_move = 10
        self.x_move = 10
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_speed = 0.09

    def move(self):
        next_x = self.xcor() + self.x_move
        next_y = self.ycor() + self.y_move
        self.goto(next_x, next_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_ball(self):
        self.move_speed = 0.09
        self.goto(0,0)
        self.bounce_x()