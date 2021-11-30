from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.paddle_bounce()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()

    if scoreboard.l_point == 10:
        print("left Player won the game")
        scoreboard.goto(0, 0)
        scoreboard.write("Game Over", align="center", font=("Courier", 80, "normal"))
        game_is_on = False

    if scoreboard.r_point == 10:
        print("Right Player won the game")
        scoreboard.goto(0, 0)
        scoreboard.write("Game Over", align="center", font=("Courier", 80, "normal"))
        game_is_on = False


screen.exitonclick()