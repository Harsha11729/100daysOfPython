BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas as pd
import random
try:
    df=pd.read_csv("data/words_learn.csv")
except FileNotFoundError:
    df=pd.read_csv("data/french_words.csv")
to_learn=df.to_dict(orient="records")

curr_card={}
def move():
    global curr_card,flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    curr_card=random.choice(to_learn)
    canvas.itemconfig(ti_text,text="French")
    canvas.itemconfig(sub_ti_text,text=curr_card['French'])
    canvas.itemconfig(canvas_img,image=card_img)
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(ti_text,text="English")
    canvas.itemconfig(sub_ti_text,text=curr_card['English'])
    canvas.itemconfig(canvas_img,image=card_img_b)
def both():
    global curr_card
    if curr_card in to_learn:
        to_learn.remove(curr_card)
    data=pd.DataFrame(to_learn)
    data.to_csv("data/words_learn.csv",index=False)
    move()
window=Tk()
window.title("Flashy")
window.config(height=626,width=900,padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)
canvas=Canvas(height=526,width=800,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)
card_img=PhotoImage(file="images/card_front.png")
card_img_b=PhotoImage(file="images/card_back.png")
canvas_img=canvas.create_image(400,263,image=card_img)
ti_text=canvas.create_text(400,150,text="French",font=("Arial",40,"italic"))
sub_ti_text=canvas.create_text(400,263,text="trouve",font=("Arial",60,"bold"))
img=PhotoImage(file="images/wrong.png")
button_1=Button(image=img,command=move)
button_1.grid(row=1,column=0)
img_2=PhotoImage(file="images/right.png")
button_2=Button(image=img_2,command=both)
button_2.grid(row=1,column=1)
move()
# -----flip cards---------------------

window.mainloop()
