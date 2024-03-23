from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Password Manager")
window.minsize(width=300, height=30)   
window.config(padx=50, pady=50)

#save all the data into a text file
def save():
    website = website_ent.get()
    email = email_ent.get()
    password = password_ent.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
    else:
        im_sure = messagebox.askokcancel(title="Website", message=f"Email: {email}\n Password: {password}\n Are you sure you want to save this?")
        if im_sure:
            with open("my_file.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_ent.delete(0, END)
                password_ent.delete(0, END)
  
#add logo
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
password_ent = Entry(width=21)
password_ent.grid(column=1, row=3)
#add a generate password button next to password entry
password_btn = Button(text="Generate Password")
password_btn.grid(column=2, row=3)
#add an add button in the last row
add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

#save all the data into a text file
def add_btn_clicked():
    f = open("my_file.txt", "a")
    f.write({})


window.mainloop()