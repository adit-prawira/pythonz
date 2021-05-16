from question import Question
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface

questionBank = []
parameters = {
    "amount":10,
    type:"boolean"
}

response = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")
response.raise_for_status()

questionData =response.json()["results"]


for question in questionData:
    questionText = question["question"]
    questionAnswer = question["correct_answer"]
    newQuestion = Question(questionText, questionAnswer )
    questionBank.append(newQuestion)


quiz = QuizBrain(questionBank)
quizUI = QuizInterface(quiz)


# while quiz.hasMoreQuestions():
#     quiz.nextQuestion()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.questionNumber}")
