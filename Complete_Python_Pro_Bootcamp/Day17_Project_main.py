from Day17_Project_data import question_data
from Day17_Project_question_class import Question
from Day17_Project_quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

d = QuizBrain(question_bank)
d.ask_qestions()