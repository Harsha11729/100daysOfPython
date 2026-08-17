from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = (
    [random.choice(letters) for _ in range(nr_letters)] +
    [random.choice(symbols) for _ in range(nr_symbols)] +
    [random.choice(numbers) for _ in range(nr_numbers)]
    )

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas=Canvas(width=200,height=200)
logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=2,row=1)
web_label=Label(text="Website: ")
web_label.grid(column=1,row=2)
web_input=Entry(width=35)
web_input.grid(column=2,row=2,columnspan=2)
web_input.focus()

def search():
    website=web_input.get()
    if website!="":
        try:
            with open("myfile.json","r") as file:
                data=json.load(file)

        except FileNotFoundError:
            messagebox.askokcancel(title="Error",message="File not found")
        else:
            if website in data:
                messagebox.askokcancel(title=website,
                                       message=f"email:{data[website]['email']},\n password:{data[website]['password']}")
            else:
                messagebox.showerror(title="Error MSG", message="Record not found")
    else:
        messagebox.askretrycancel(title="Vacancyerror",message="Don't leave something blank")
web_search=Button(text="Search",command=search)
web_search.grid(column=4,row=2)
user_label=Label(text="Email/Username: ")
user_label.grid(column=1,row=3)
user_input=Entry(width=35)
user_input.grid(column=2,row=3,columnspan=2)
user_input.insert(END,"@gmail.com")
pass_label=Label(text="Password: ")
pass_label.grid(column=1,row=4)
pass_input=Entry(width=21)
pass_input.grid(column=2,row=4)
pass_button=Button(text="Generate Password",command=generate_password)
pass_button.grid(column=3,row=4)

def add():
    if web_input.get()=="" or pass_input.get()=="":
        messagebox.askretrycancel(title="oops",message="Don't leave any blank empty")
    else:
        is_ok = messagebox.askokcancel(title="Website",message="Are you ok to continue with these details")
        if is_ok:
            content_web = web_input.get()
            content_user = user_input.get()
            content_pass = pass_input.get()
            new_data={
                content_web:{
                    "email":content_user,
                    "password":content_pass,
                }
            }
            try:
                with open("myfile.json","r") as file:
                    data=json.load(file)
            except FileNotFoundError:
                with open("myfile.json","w") as file:
                    json.dump(new_data,file)
            else:
                data.update(new_data)
                with open("myfile.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                web_input.delete(0,END)
                user_input.delete(0,len(user_input.get())-10)
                pass_input.delete(0,END)

add_button= Button(text="Add",command=add)
add_button.grid(column=2,row=5)

window.mainloop()