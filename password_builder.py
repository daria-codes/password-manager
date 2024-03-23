from tkinter import *

window = Tk()
window.title("Password Manager")
window.minsize(width=300, height=30)   
window.config(padx=50, pady=50)

#add logo
canvas = Canvas( window, width=400, height=300)
logo = PhotoImage(file="logo.png")
canvas.create_image(50,85, image=logo)
canvas.grid(column=0, row=0, columnspan=2)


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
website_ent = Entry(width=40)
website_ent.grid(column=1, row=1, columnspan=2 )
#add entry next to email/username text
username_ent = Entry(width=40)
username_ent.grid(column=1, row=2, columnspan=2)
#add entry next to password text
password_ent = Entry(width=18)
password_ent.grid(column=1, row=3)
#add a generate password button next to password entry
password_btn = Button(text="Generate Password")
password_btn.grid(column=2, row=3)
#add an add button in the last row
add_btn = Button(text="Add", width=38)
add_btn.grid(column=1, row=4, columnspan=2)





window.mainloop()