from tkinter import *

window = Tk()
window.title("Password Manager")
window.minsize(width=500, height=300)   
window.config(padx=20, pady=20)

canvas = Canvas( window, width=400, height=400)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=3, row=1)


#add website text
#add Email/Uswername text
#add password text
#add an add button in the last row
#add entry next to website text
#add entry next to email/username text
#add entry next to password text
#add a generate password button next to password entry







window.mainloop()