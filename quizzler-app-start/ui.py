from tkinter import *
import time
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.score=0
        self.window=Tk()
        self.quiz=quiz_brain
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.label=Label(text=f"Score:{self.quiz.score}",bg=THEME_COLOR,fg="white")
        self.label.grid(column=1,row=0,columnspan=2)
        self.canvas=Canvas(width=300,height=250,bg="white")
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)
        self.question_text=self.canvas.create_text(150,125,text="some text",width=280)
        true_img=PhotoImage(file="images/true.png")
        self.button_right=Button(image=true_img,highlightthickness=0,command=lambda :self.both("true"))
        self.button_right.grid(column=0,row=2)
        false_img=PhotoImage(file="images/false.png")
        self.button_wrong=Button(image=false_img,highlightthickness=0,command=lambda:self.both("false"))
        self.button_wrong.grid(column=1,row=2)
        self.quiz_next_ques()


        self.window.mainloop()
    def quiz_next_ques(self):
        q_text=self.quiz.next_question()
        self.canvas.itemconfig(self.question_text,text=q_text)
        self.button_right.config(state="normal")
        self.button_wrong.config(state="normal")

    def both(self,answer):

        self.button_right.config(state="disabled")
        self.button_wrong.config(state="disabled")
        if self.quiz.question_number<len(self.quiz.question_list):
            if self.quiz.check_answer(answer):
                self.canvas.config(bg="green")
            else:
                self.canvas.config(bg="red")
            self.label.config(text=f"Score:{self.quiz.score}",bg=THEME_COLOR,fg="white")
            self.window.after(2000,lambda:[self.quiz_next_ques(),self.canvas.config(bg="white")])





        else:
            self.canvas.itemconfig(self.question_text, text="...WE ARE PROCESSING YOUR FINAL SCORE....")
            self.window.after(3000,lambda:self.canvas.itemconfig(self.question_text, text=f"Your Final score is {self.quiz.score}"))

