from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter as tk
from tkinter import PhotoImage
from guest_app import *
from reservation_app import *
from room_app import *

def room_management():

    pass

def guest_management():
  pass
def reservation_management():
  pass


window = Tk()
window.geometry("600x600")
window.title("Hotel System")
window.config(cursor="hand2" , background="snow3")

title_lable=Label(window , text="Hotel System" , font=("Arial", 30 , "bold") , background="snow3").place(x=20 , y=20)

Button(window , text="Room management" , command=room_management , width=20).place(x=20 , y=100)
Button(window , text="Guest management" , command=guest_management , width=20).place(x=20 , y=243)
Button(window , text="Reservation management" , command=reservation_management , width=20).place(x=20 , y=385)




img=Image.open("hotel.png")
img=img.resize((300,300))
img=ImageTk.PhotoImage(img)
my_lable=Label(window , image=img)
my_lable.place(x=300, y=100)










window.mainloop()


