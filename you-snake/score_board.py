from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("#c5da9e")
        self.hideturtle()
        self.penup()
        self.goto(230, 270)
        self.refresh_score()
    
    def add_score(self):
        self.score += 1
        self.clear()
        self.refresh_score()
        
    def refresh_score(self):
        self.write(
            f"Score: {self.score}", 
            align = "center", 
            font=("Arial", 24 , "normal")
        )