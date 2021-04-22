from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#9bbafa")
        self.penup()
        self.refresh_loc()
        
    
    def refresh_loc(self):
        # stretch the size of the turtle by half (shrink)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        
        # randomly set its position within the screen
        self.goto(rand_x, rand_y)