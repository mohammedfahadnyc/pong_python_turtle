import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
HEIGHT = 600
WIDTH = 800

screen = Screen()
screen.bgcolor("black")
screen.setup(height=HEIGHT,width=WIDTH)
screen.title("Welcome To Pong!")
screen.tracer(0)

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key="Up",fun=r_paddle.move_up)
screen.onkey(key="Down",fun=r_paddle.move_down)
screen.onkey(key="w",fun=l_paddle.move_up)
screen.onkey(key="s",fun=l_paddle.move_down)

is_game_on = True
while is_game_on :
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()
    if (ball.xcor() > 320 and r_paddle.distance(ball) < 50)  or (ball.xcor() < -320  and l_paddle.distance(ball) < 50) :
        ball.bounce_x()
    if (ball.xcor() > 400 and r_paddle.distance(ball) > 50)  :
        ball.reset_position()
        scoreboard.l_score += 1
        scoreboard.update_score()
    if (ball.xcor() < -400  and l_paddle.distance(ball) > 50) :
        ball.reset_position()
        scoreboard.r_score += 1
        scoreboard.update_score()



screen.exitonclick()