from turtle import Turtle,Screen
import pandas as pd

screen=Screen()
screen.title("Guess the state")
turtle=Turtle()
score=Turtle()
score.hideturtle()
score.penup()
countries=[]
missing_countries=[]
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
with open("50_states.csv", mode='r') as data:
    data_in_file = pd.read_csv(data)
state_col = data_in_file.state.str.lower()
x_col = data_in_file.x
y_col = data_in_file.y
is_game=True
while is_game:
    answer_state=screen.textinput(title="Guess the state",prompt="Enter next State:").lower()
    if answer_state is None:
        continue
    if len(countries)==len(state_col) or answer_state=="exit":
        is_game=False
        missing_countries=[state_col[col] for col in range(len(state_col)) if state_col[col] not in countries]
        df=pd.DataFrame(missing_countries,columns=['Miss States'])
        df.to_csv('missing_countries.csv',columns=['Miss States'])
    else:
        for col in range(len(state_col)):
            if state_col[col]==answer_state:
                score.goto(x_col[col],y_col[col])
                score.write(answer_state)
                if state_col[col] not in countries:
                    countries.append(answer_state)

