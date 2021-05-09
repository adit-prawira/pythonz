from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("#c5da9e")
        self.penup()
        self.hideturtle()

        self.left_score = 0
        self.right_score = 0
        self.updateScoreBoard()
    
    def updateScoreBoard(self):
        self.goto(0, 200)
        self.write(f"{self.left_score} - {self.right_score}", align="center", font = ("Courier", 80, "normal"))
        
    def addRightScore(self):
        self.right_score += 1
        self.clear()
        self.updateScoreBoard()
    
    def addLeftScore(self):
        self.left_score += 1
        self.clear()
        self.updateScoreBoard()