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
        self.scoreLabel = Label(text=f"Score:{self.quiz.score}", bg = THEME_COLOR, fg = "white")
        
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
        self.trueButton = Button(image = trueLogo, highlightthickness=0, command = self.answerTrue)
        self.trueButton.grid(row = 2, column = 0)
        
        falseLogo = PhotoImage(file = "images/false.png")
        self.falseButton = Button(image = falseLogo, highlightthickness=0, command = self.answerFalse)
        self.falseButton.grid(row = 2, column = 1)
        
        self.getNextQuestion()
        self.window.mainloop()
        
    def getNextQuestion(self):
        self.canvas.config(bg = "white")
        if(self.quiz.hasMoreQuestions()):
            self.scoreLabel.config(text=f"Score:{self.quiz.score}")
            qText = self.quiz.nextQuestion()
            self.canvas.itemconfig(self.questionText, text = qText)
        else:
            self.canvas.itemconfig(self.questionText, text = "You've reached the end of the quiz")
            self.trueButton.config(state="disabled")
            self.falseButton.config(state="disabled")
    def answerTrue(self):
        self.giveFeedback(self.quiz.checkAnswer("True"))
    
    def answerFalse(self):
        self.giveFeedback(self.quiz.checkAnswer("False"))
    
    def giveFeedback(self, isRight):
        if isRight:
            self.canvas.config(bg = "#d3e9a6")
        else:
            self.canvas.config(bg = "#f07684")
            
        self.window.after(1000, self.getNextQuestion)
        