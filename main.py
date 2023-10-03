from tkinter import Tk, Canvas, PhotoImage, Button, messagebox
import pandas
import random
current_card = {}
to_learn = {}
BG_COLOR = "#B1DDC6"



# ---------------------------- GENERATE RANDOM WORD ------------------------- #

try: 
    data = pandas.read_csv("./Data/words_to_learn.csv")
except FileNotFoundError:
    try:
        original_data = pandas.read_csv("./Data/english_words.csv")
        to_learn = original_data.to_dict(orient="records")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="File not found")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=font_img)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./Data/words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------- #
window = Tk()
window.title("Flash Cards")
window.config(bg=BG_COLOR, padx=100)
window.minsize(width=1000, height=800)

# Canvas
font_img = PhotoImage(file="./images/card_front.png")
background_img = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BG_COLOR)
card_background = canvas.create_image(400, 526/2, image=font_img)
card_title = canvas.create_text(400, 100, text="English",
                                font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 300, text="Example polish word",
                               font=("Arial", 50, "bold"))
canvas.grid(row=0, column=0, columnspan=2, pady=50)

# Buttons
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, width=wrong_img.width(),
                      height=wrong_img.height(), highlightthickness=0, borderwidth=0, bg=BG_COLOR, command=next_card)
wrong_button.grid(row=1, column=0, sticky="n")

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, width=right_img.width(),
                      height=right_img.height(), highlightthickness=0, borderwidth=0, bg=BG_COLOR, command=is_known)
right_button.grid(row=1, column=1, sticky="n")

window.mainloop()