import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    timer_text.config(text="00.00")
    label.config(text="Timer")
    marks=""
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    if reps%8==0:
        label.config(text='Break',fg=RED)
        count_down(long_break_sec)
    elif reps % 2==0:
        label.config(text='Break', fg=PINK)
        count_down(short_break_sec)
    else:
        label.config(text='Work', fg=GREEN)
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✓"
        checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW,highlightthickness=0)
canvas=Canvas(width=200,height=224)
tom_image=PhotoImage(file="tomato.png")
canvas.create_image(102,112,image=tom_image)
timer_text=canvas.create_text(103,130,text="00.00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)
label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,25,'bold'))
label.grid(column=2,row=1)
button_1=Button(text="Start",bg=YELLOW,highlightthickness=0,command=start_timer)
button_1.grid(column=1,row=3)
button_2=Button(text="Reset",bg=YELLOW,command=reset)
button_2.grid(column=3,row=3)
checkmark=Label(text="✓",fg=GREEN,bg=YELLOW)
checkmark.grid(column=2,row=3)
def st_button():
    start_timer()
window.mainloop()