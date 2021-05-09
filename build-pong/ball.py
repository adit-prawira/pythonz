from turtle import Turtle

class Ball (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#c46a7e")
        self.penup()
        self.goto((0,0))
        self.x_move = 10
        self.y_move = 10
        self.speed = 0.05
        
    def move(self):
        newX = self.xcor() + self.x_move
        newY = self.ycor() + self.y_move
        self.goto((newX, newY))
        
    # bounce with the wall 
    def bounceY(self):
        self.y_move *= -1
        self.speed *= 0.9
        
    def bounceX(self):
        self.x_move *= -1
        self.speed *= 0.9
        
    def reset(self):
        self.goto((0,0))
        self.speed = 0.05
        self.bounceX()
        
    