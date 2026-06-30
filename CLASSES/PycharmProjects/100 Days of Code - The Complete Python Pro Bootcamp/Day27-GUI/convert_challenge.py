from tkinter import *


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width = 300, height = 100 )

entry = Entry(width=12)
#Add some text to begin with
entry.insert(END, string="0")
entry.grid(row=0,column=1)
#Label
miles_label = Label(text = "Miles", font=("Arial",12))
miles_label.grid(row=0, column=2)

isequal_label = Label(text = "    is equal to", font=("Arial",12))
isequal_label.grid(row=1, column=0)

answer_label = Label(text = " 0 ", font=("Arial",12))
answer_label.grid(row=1, column=1)

km_label = Label(text = "km", font=("Arial",12))
km_label.grid(row=1, column=2)
#Button
def button_clicked():
    miles = float(entry.get())
    km = miles*1.609
    answer_label.config(text=str(km))

button = Button(text="Calculate", command=button_clicked)
button.grid(row=2,column=1)

window.mainloop()
