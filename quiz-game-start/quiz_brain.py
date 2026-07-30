class QuizBrain:
    def __init__(self,q_list):
        self.question_no=0
        self.question_list=q_list
        self.score=0

    def still_has_question(self):
        return self.question_no < len(self.question_list)
    def next_question(self):
        current_question=self.question_list[self.question_no]
        self.question_no+=1
        user_ans=input(f"Q{self.question_no}:{current_question.text}?:").lower()
        self.check_answer(user_ans,current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer==correct_answer.lower():
            print("your answer is correct")
            self.score+=1
        else:
            print("your answer is wrong")
        print(f"your current score is {self.score}/{self.question_no}")
        print(f"correct answer is {correct_answer}")