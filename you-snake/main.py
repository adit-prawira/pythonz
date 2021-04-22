from turtle import Turtle, Screen
from snake import Snake
import time

# Screen set up
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("#373c4e")
screen.title("You Snake!")
screen.tracer(0)

snake = Snake()

screen.listen()

# command keys
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

has_started = True
while has_started:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
screen.exitonclick()