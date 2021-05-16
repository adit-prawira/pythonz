import html
class QuizBrain:
    def __init__(self, inputList):
        self.score = 0;
        self.questionNumber = 0;
        self.questionList= inputList
        self.currentQuestion = None
        
    def hasMoreQuestions(self):
        return self.questionNumber < len(self.questionList)
    
    def nextQuestion(self):
        self.currentQuestion = self.questionList[self.questionNumber]
        self.questionNumber += 1
        questionText = html.unescape(self.currentQuestion.text)
        return f"Q.{self.questionNumber}: {questionText} (True/False): "

    def checkAnswer(self, userAnswer):
        correctAnswer = self.currentQuestion.answer
        if userAnswer.lower() == correctAnswer.lower():
            self.score += 1
            return True
        else:
            return False