from tkinter import *

#tkinter created from another language
# - plethora of [optional arguments] prevents argument prompting and documentation pop

window = Tk()
window.title("My First GUI Program")
window.minsize(width = 500, height = 300 )

#Label
my_label = Label(text = "I am a Label", font=("Arial",24, "italic"))
my_label.pack()

my_label["text"] ="New Text"
my_label.config(text="New Text")
my_label["foreground"] = "blue"

#Button
def button_clicked():
    print("I got clicked")
    s=input.get()
    my_label.config(text=s)

button = Button(text="Click Me", command=button_clicked)
button.pack()

#Entry
input = Entry(width = 50)
input.pack()
# import turtle
# tim =turtle.Turtle()
# tim.write("some text",font=("T"))
# Keeps window from closing, keep last
window.mainloop()
