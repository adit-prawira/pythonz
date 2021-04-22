from turtle import Turtle, Screen
from paddle import Paddle
import time
#Screen set up
screen = Screen()
screen.setup(width = 800, height = 600)
screen.bgcolor("#373c4e")
screen.title("Build Pong")
screen.tracer(0)

right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
screen.listen()

# right paddle with up and down key control
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

# left paddle with w and s key to control vertical movement
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

is_started = True
while is_started:
    screen.update()
    time.sleep(0.1)
    

screen.exitonclick()