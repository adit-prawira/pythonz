THEME_COLOR = "#373c4e"
from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain

class QuizInterface :
    def __init__(self, quizBrain: QuizBrain):
        self.quiz = quizBrain
        self.window = Tk()
        self.window.title("Quiz Me")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)
        self.scoreLabel = Label(text=f"Score:{0}", bg = THEME_COLOR, fg = "white")
        
        self.scoreLabel.grid(row = 0, column = 1)
        
        self.canvas = Canvas(height = 250, width = 300, bg = "white")
        self.questionText = self.canvas.create_text(
            150, 125, 
            width = 280,
            text = "Some Text", 
            fill = THEME_COLOR,
            font = ("Arial", 20, "italic")
        )
        self.canvas.grid(row = 1, column =0 , columnspan = 2, pady = 50)
        
        trueLogo = PhotoImage(file = "images/true.png")
        self.trueButton = Button(image = trueLogo, highlightthickness=0)
        self.trueButton.grid(row = 2, column = 0)
        
        falseLogo = PhotoImage(file = "images/false.png")
        self.falseButton = Button(image = falseLogo, highlightthickness=0)
        self.falseButton.grid(row = 2, column = 1)
        
        self.getNextQuestion()
        self.window.mainloop()
        
    def getNextQuestion(self):
        qText = self.quiz.nextQuestion()
        print(qText)
        self.canvas.itemconfig(self.questionText, text = qText)
        