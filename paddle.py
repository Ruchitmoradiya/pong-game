from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.setheading(90)
        self.penup()
        self.goto(position)

    def up(self):
        self.forward(20)

    def down(self):
        self.back(20)

