from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# The goal is to create a question bank List holds the data we received i the data file
question_bank = []
for item in question_data:
    question_text = item["text"]
    question_answer = item["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score is {quiz.score}/{len(quiz.question_list)}")
