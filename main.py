from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
choose = {}
data_dict = {}
# Reading data csv file
try:
    data = pd.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('data/french_words.csv')
    data_dict=original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

# Button command
def next_card():
    global choose, flip_timer
    windows.after_cancel(flip_timer)
    choose = random.choice(data_dict)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=choose['French'], fill= 'black')
    canvas.itemconfig(card_image, image= card_front)
    flip_timer = windows.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=choose['English'], fill='white')
    canvas.itemconfig(card_image, image=card_back)

def is_known():
    data_dict.remove(choose)
    data1 = pd.DataFrame(data_dict)
    data1.to_csv("data/words_to_learn.csv", index = False )

    next_card()

# Creating user interface
windows = Tk()
windows.title("Flash-Card")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer= windows.after(3000, func= flip_card)

canvas = Canvas(width=800, height=526, bg= BACKGROUND_COLOR, highlightthickness=0)

# Creating French-card and English-card page
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image= card_front)
card_title = canvas.create_text(400, 150, text = '',font=('Ariel',30,'italic'))
card_word = canvas.create_text(400, 263, text ='', font=('Ariel', 40, 'bold'))
canvas.grid(row=1, column= 1, columnspan=2)


# Creating Right Button
right_img = PhotoImage(file= "images/right.png")
r_button = Button(image=right_img, bg=BACKGROUND_COLOR, highlightthickness= 0, command= is_known)
r_button.grid(row= 2, column= 2)


# Creating wrong button
wrong_img = PhotoImage(file="images/wrong.png")
w_button = Button(image=wrong_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
w_button.grid(row=2, column= 1)

next_card()

windows.mainloop()
