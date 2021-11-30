from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_point = 0
        self.r_point = 0
        self.color("White")
        self.penup()
        self.hideturtle()
        self.updateboard()

    def updateboard(self):
        self.clear()
        self.goto(-100, 220)
        self.write(self.l_point, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 220)
        self.write(self.r_point, align="center", font=("Courier", 50, "normal"))

    def left_point(self):
        self.l_point += 1
        self.updateboard()

    def right_point(self):
        self.r_point += 1
        self.updateboard()



