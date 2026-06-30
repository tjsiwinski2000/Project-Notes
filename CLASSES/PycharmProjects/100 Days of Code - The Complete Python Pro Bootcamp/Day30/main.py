from time import sleep
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# -------------Data Section---------------------
# open words_to_learn if exists, otherwise default to french_words.csv
try:
    my_data_frame = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    my_data_frame = pandas.read_csv("data/french_words.csv")
to_learn = my_data_frame.to_dict(orient='records')
print(to_learn)

# current_card has to be a global
current_card ={}

def known_word():
    global current_card
    #remove last word from current list note: current_card is a dictionary{} e.g. {'Unnamed: 0': 0, 'French': 'histoire', 'English': 'history'},
    to_learn.remove(current_card)
    #save updated data to [words_to_learn.csv]
    update_data_frame = pandas.DataFrame(to_learn)
    # index = false prevent addition of index column for each "session"
    update_data_frame.to_csv("data/words_to_learn.csv")
    next_card()

def next_card():
    #works but not the cleanest
    # choice = random.randint(0, len(to_learn) - 1)
    # print(f"{to_learn[choice]['French']} => {to_learn[choice]['English']}")

    #tap into global current_card declared on line #14
    global  current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    print(current_card['French'])
    print(current_card['English'])
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word,text=current_card['French'], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    #this is dope, reset the global var flip_timer to prevent bug
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English",fill = "white")
    canvas.itemconfig(card_word,text=current_card['English'],fill = "white")
    canvas.itemconfig(card_background, image = card_back_image)

# -------------UserInterface---------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

# note: do not use sleep with tkinter , window(or whatever main variable is)
flip_timer = window.after(3000,flip_card)

canvas = Canvas(width = 800, height = 526)
card_front_image = PhotoImage(file = "images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)

# remember 400,150 is "relative" to the canvas , thus 400 is 1/2 way, 150 is top 1/3
card_title=canvas.create_text(400,150,text="Title", font = ("Ariel", 40, "italic"))
card_word=canvas.create_text(400,263, text="word", font = ("Ariel", 60, "bold"))

canvas.config(bg= BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0,command=next_card)
unknown_button.grid(row=1, column=0)
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image,highlightthickness=0,command=known_word)
known_button.grid(row=1, column=1)


next_card()
window.mainloop()
