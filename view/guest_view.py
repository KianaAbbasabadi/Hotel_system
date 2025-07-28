from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox as msg
from controller.guest_controller import GuestController
def save_guest():
    pass
def edite_guest():
    pass
def delete_guest():
    pass
def reset_guest():
    pass
def search_guest():
    pass

window = Tk()
window.title("Guest View")
window.geometry("800x800")
window.config(cursor="hand2", background="snow3")
img=Image.open('guest.png')
img = img.resize((250, 100))
img=ImageTk.PhotoImage(img)
my_label=Label(window , image=img)
my_label.place(x=20 , y=20)

#guest_code
Label(window , text="Guest code").place(x=20, y=150)
guest_code=IntVar()
Entry(window, textvariable=guest_code).place(x=150, y=150)

#name
Label(window , text="Name").place(x=20, y=200)
name=StringVar()
Entry(window, textvariable=name).place(x=150, y=200)
#family
Label(window , text="Family").place(x=20, y=250)
family=StringVar()
Entry(window, textvariable=family).place(x=150, y=250)
#age
Label(window , text="Age").place(x=20, y=300)
age=IntVar()
Entry(window, textvariable=age).place(x=150, y=300)
#phone number
Label(window , text="Phone number").place(x=20, y=350)
phone_number=StringVar()
Entry(window, textvariable=phone_number).place(x=150, y=350)
#birth date
Label(window , text="Birth date").place(x=20, y=400)
birth_date=StringVar()
Entry(window, textvariable=birth_date).place(x=150, y=400)

guest_table=ttk.Treeview(window , columns=[1 , 2, 3, 4, 5 ,6 ] , show="headings")
guest_table.heading(1 , text="Guest Code")
guest_table.heading(2, text="Name")
guest_table.heading(3, text="Family")
guest_table.heading(4, text="Age")
guest_table.heading(5, text="Phone number")
guest_table.heading(6, text="Birth date")

guest_table.column(1 , width=100 , anchor=CENTER)
guest_table.column(2, width=150 , anchor=CENTER)
guest_table.column(3, width=150 , anchor=CENTER)
guest_table.column(4, width=150 , anchor=CENTER)
guest_table.column(5, width=150 , anchor=CENTER)
guest_table.column(6, width=150, anchor=CENTER)
guest_table.place(x=350, y=150)

Button(window, text="Save", width=18, command=save_guest).place(x=20, y=550)
Button(window, text="edit", width=18, command=edite_guest).place(x=180, y=550)
Button(window, text="delete", width=18, command=delete_guest).place(x=20, y=580)
Button(window, text="clear", width=18, command=reset_guest).place(x=180, y=580)
Button(window, text="search", width=41, command=search_guest).place(x=20, y=610)





window.mainloop()