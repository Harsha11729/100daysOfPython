import tkinter
window=tkinter.Tk()
window.title("This is my first GUI")
window.minsize(500,300)
my_label=tkinter.Label(text='New text',font=('Arial',32))
my_label.grid(column=0,row=0)
def button_click():
    my_label["text"] = input.get()

button=tkinter.Button(text='Click Me',command=button_click)
button.grid(column=2,row=2)
button1=tkinter.Button(text='new_butt')
button1.grid(column=3,row=0)
input=tkinter.Entry(width=15)
input.grid(column=4,row=3)

window.mainloop()