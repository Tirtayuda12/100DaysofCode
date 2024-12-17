#Quiz Game Project
from data import question_data
from question_model import Question
from quiz_brain import QuizzBrain
question_bank = []
for question in question_data:
    q_text = question['text']
    q_answer = question['answer']
    newQuestion = Question(q_text,q_answer)
    question_bank.append(newQuestion)


quizz = QuizzBrain(question_bank)
to_continue = True

while to_continue:
    to_continue = quizz.still_has_questions()
    quizz.next_question()

print("You`ve completed the quiz")
print(f"Your final score was:{quizz.score}/{quizz.question_number}")
    

