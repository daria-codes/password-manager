from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json 

window = Tk()
window.title("Password Manager")
window.minsize(width=300, height=30)   
window.config(padx=50, pady=50)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
numbers = ['1','2','3','4','5','6','7','8','9']
symbols = ['!','$','%','^','&','*','-']

password_letters = [choice(letters) for _ in range(randint(6,8))]
password_numbers = [choice(numbers) for _ in range(randint(3,5))]
password_symbols = [choice(symbols) for _ in range(randint(2,4))]

password_list = password_letters + password_numbers + password_symbols

shuffle(password_list)

password = "".join(password_list)

def generate_password():
    password_ent.insert(0, password)
    pyperclip.copy(password) #copies the password generated 
#save all the data into a text file
def save():
    website = website_ent.get() 
    email = email_ent.get()
    password = password_ent.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        with open("my_file.json", "r") as data_file:
            #Reading old data
            data = json.load(data_file)
            #Updating old data with new data
            data.update(new_data)
        with open("my_file.json", "w") as data_file:
            #Saving updated data
            json.dump(data, data_file, indent=4)
            
            website_ent.delete(0, END)
            password_ent.delete(0, END)
  
#add image
canvas = Canvas( window, width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(50,100, image=logo)
canvas.grid(column=1, row=0, columnspan=2)


#add website text
website_txt = Label(text="Website", width=12)
website_txt.grid(column=0, row=1)
#add Email/Uswername text
username_txt = Label(text="Email/Username", width=12)
username_txt.grid(column=0, row=2)
#add password text
password_txt = Label(text="Password", width=12)
password_txt.grid(column=0, row=3)

#add entry next to website text
website_ent = Entry(width=35)
website_ent.grid(column=1, row=1, columnspan=2 )
website_ent.focus()
#add entry next to email/username text
email_ent = Entry(width=35)
email_ent.grid(column=1, row=2, columnspan=2)
email_ent.insert(0,"dcode@gmail.com")
#add entry next to password text
password_ent = Entry()
password_ent.grid(column=1, row=3)
#add a generate password button next to password entry
password_btn = Button(text="Generate Password", command=generate_password)
password_btn.grid(column=2, row=3)
#add an add button in the last row
add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

#save all the data into a text file
def add_btn_clicked():
    f = open("my_file.txt", "a")
    f.write({})


window.mainloop()