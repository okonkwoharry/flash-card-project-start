BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random

window = Tk()
window.title("Flashy")
window.minsize()
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
count = -1


def button_press():
    global count
    count += 1
    number = random.randint(0, 100)
    canvas.itemconfig(word_text, text=french_data[number], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    if count >= 0:
        french_data.pop(number)


    def bbb():
        canvas.itemconfig(canvas_image, image=card_back_img)
        canvas.itemconfig(word_text, text=english_data[number], fill="white")
        canvas.itemconfig(title_text, text="English", fill="white")
        if count >= 0:
            english_data.pop(number)

    canvas.after(3000, bbb)


def button_press_bad():
    global count
    count += 1
    number = random.randint(0, 100)
    canvas.itemconfig(word_text, text=french_data[number], fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(title_text, text="French", fill="black")
    if count >= 0:
        with open("words_to_learn.csv", "a") as file:
            file.write(f"{french_data[number]},{english_data[number]}\n")



    def bbb():
        canvas.itemconfig(canvas_image, image=card_back_img)
        canvas.itemconfig(word_text, text=english_data[number], fill="white")
        canvas.itemconfig(title_text, text="English", fill="white")


    canvas.after(3000, bbb)



canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
word_text = canvas.create_text(400, 260, text="Word", fill="black", font=("Arial", 43, "bold"))
title_text = canvas.create_text(400, 160, text="Title", fill="black", font=("Arial", 34, "normal"))



cancel_img = PhotoImage(file="images/wrong.png")
cancel_button = Button(image=cancel_img, highlightthickness=0, borderwidth=0, command=button_press_bad)
cancel_button.grid(column=0, row=1)


correct_img = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_img, highlightthickness=0, borderwidth=0, command=button_press)
correct_button.grid(column=1, row=1)

data = pandas.read_csv("data/french_words.csv")
data_dic = data.to_dict()
french_data = data_dic["French"]
english_data = data_dic["English"]






window.mainloop()