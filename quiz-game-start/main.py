from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for question in question_data:
    text=question['question']
    answer=question['correct_answer']
    new_ques=Question(text,answer)
    question_bank.append(new_ques)
play=QuizBrain(question_bank)
while play.still_has_question():
    play.next_question()
print("you have completed the quiz")
print(f"your final score is {play.score}/{play.question_no}")