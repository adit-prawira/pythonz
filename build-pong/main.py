from turtle import Turtle, Screen
from paddle import Paddle
import time
#Screen set up
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("#373c4e")
screen.title("Build Pong")
screen.tracer(0)

paddle = Paddle()

screen.listen()
screen.onkey(paddle.move_up, "Up")
screen.onkey(paddle.move_down, "Down")

is_started = True
while is_started:
    screen.update()
    time.sleep(0.1)
    

screen.exitonclick()