from turtle import Turtle\

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 20
        self.ymove = 20

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def wall_bounce(self):
        self.ymove *= -1

    def paddle_bounce(self):
        self.xmove *= -1


    def reset_position(self):
        self.goto(0, 0)
        self.xmove *= -1
        self.ymove *= -1
