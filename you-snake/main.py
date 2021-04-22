from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

# Screen set up
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("#373c4e")
screen.title("You Snake!")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()

# command keys
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

is_started = True

while is_started:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # check for collision between snake's head and food
    # turtle.distance(another_turtle) 
    if(snake.head.distance(food) < 15 ):
        food.refresh_loc()
        snake.grow()
        score_board.add_score()
        
    # collision with wall
    if(snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280):
        is_started = False
        score_board.game_over()
    
    # collision with tail
    for seg in snake.segs[1:]:
        if(snake.head.distance(seg) < 10):
            is_started = False
            score_board.game_over()
screen.exitonclick()