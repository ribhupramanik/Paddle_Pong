from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.title("Paddle Pong Game")
screen.bgcolor("black")
screen.tracer(0)
scoreboard = Scoreboard()

right_paddle = Paddle(350,0)
left_paddle = Paddle(-350,0)
ball = Ball()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    scoreboard.update_scoreboard()

#checking wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

#Detection of collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() >320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #detecting out-of-bounds right side
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    # detecting out-of-bounds left side
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()