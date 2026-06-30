from tkinter import *
# messagebox must be imported separately
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

    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    password_list += [random.choice(letters) for char in range(nr_letters) ]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    password_list += [random.choice(symbols) for char in range(nr_symbols)]

    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    password = "".join(password_list)
    pyperclip.copy(password)

    print(f"Your password is: {password}")
    Password_entry.insert(0,password)
# ---------------------------- FIND PASSWORD--------------------------- #
def find_password():
    # Handle file DNE
    try:
        with open("data.json", "r") as data_file:
            # READ serialize JSON (existing data) => python dictionary
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="oops", message="No Data File Found")
    else:
        web = Website_entry.get()
        entry = data.get(web)
        if entry == None:
            messagebox.showinfo(title="oops", message=f"No details for {web} exists")
        else:
            user_info_found = f"Email: {entry['email']}\nPassword: {entry["password"]}"
            messagebox.showinfo(title=web, message=user_info_found)



# ---------------------------- SAVE PASSWORD ------------------------------- #
#take website, email, user, ->data.txt when [add] clicked, also clear all Entry boxes after file written
def save_data():
    s1= Email_UserName_entry.get()
    s2 = Website_entry.get()
    s3= Password_entry.get()
    new_data={
        s2: {
            "email" : s1,
            "password" : s3
        }
    }
    if len(s2) == 0 or len(s3) ==0:
        messagebox.showinfo(title="oops", message="Please don't leave any fields empty!")
        return
    else:
        line = f"{s1}|{s2}|{s3}\n"

        # is_ok = messagebox.askokcancel(title=f"{s2}" , message=f"These are the details entered: \nEmail:{s1}\nPassword: {s3} \nIs it okay to save?")
        # if is_ok:
        try:
            with open("data.json","r") as data_file:
                # READ serialize JSON (existing data) => python dictionary
                data=json.load(data_file)
        except FileNotFoundError:
            # - file DNE, create file, write to it
            with open("data.json", 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # UPDATE with new_data (latest website, userid, pass in dictionary format)
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # WRITE python dictionary => JSON, file
                json.dump(data, data_file, indent=4)

        finally:
            Website_entry.delete(0,END)
            Password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
#canvas widget
canvas = Canvas(width=200, height=200)
#photo image class
main_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image= main_img)
canvas.grid(row=0, column=1)

# emplace Website label and text box
Website_label= Label(text = "Website:", fg = "black", bg= "white",font= ("Ariel", 10))
Website_label.grid(row=1,column=0)
Website_entry = Entry(width =21)
Website_entry.grid(row =1,column=1)
Website_entry.focus()
search_button = Button(text="Search", command=find_password, highlightthickness=0, width=13)
search_button.grid(row=1,column=2)

Email_UserName__label= Label(text = "Email\\UserName:", fg = "black", bg= "white",font= ("Ariel", 10))
Email_UserName__label.grid(row=2,column=0)
Email_UserName_entry = Entry(width =40)
Email_UserName_entry.grid(row =2,column=1, columnspan=2)
Email_UserName_entry.insert(0,'tjsiwinski_2000@yahoo.com')
Password_label= Label(text = "Password:", fg = "black", bg= "white",font= ("Ariel", 10))
Password_label.grid(row=3,column=0)
Password_entry = Entry(width =21)
Password_entry.grid(row =3,column=1)
#Buttons
gen_pass_button = Button(text="Generate Password", command=generate_password, highlightthickness=0)
gen_pass_button.grid(row=3,column=2)
add_pass_button = Button(text="Add", command=save_data, highlightthickness=0,width=44)
add_pass_button.grid(row=4,column=1,columnspan=2)
window.mainloop()