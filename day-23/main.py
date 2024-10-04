from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(text_param=question_text,
                            answer_param=question_answer)
    question_bank.append(new_question)

quiz_game = QuizBrain(question_bank)

while quiz_game.still_has_questions():
    quiz_game.next_question()
