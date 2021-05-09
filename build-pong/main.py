from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard

import time
#Screen set up
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("#373c4e")
screen.title("Build Pong")
screen.tracer(0)

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()
score = ScoreBoard()

screen.listen()

# right paddle with up and down key control
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

# left paddle with w and s key to control vertical movement
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

is_started = True

while is_started:
    time.sleep(ball.speed)
    screen.update()
    ball.move()
    
    # Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()
    
    # Collision with left and right paddle
    if((ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320)):
        ball.bounceX()
    
    # reset ball and add score to left paddle
    if ball.xcor() > 400:
        score.addLeftScore()
        ball.reset()
    
    # reset ball and add score to right paddle
    if(ball.xcor() < -400):
        score.addRightScore()
        ball.reset()
        
screen.exitonclick()