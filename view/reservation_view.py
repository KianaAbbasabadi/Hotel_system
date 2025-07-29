from re import search
from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from controller.reservation_controller import ReservationController
from model.entity.reservation import Reservation
payment_status_list=["pending" , "paid" , "refunded" , "unpaid"]
is_cancelled_list=["Yes" , "No"]
def save_reservation():
    pass
def edit_reservation():
    pass
def delete_reservation():
    pass
def reset_reservation():
    pass
def search_reservation():
    pass


window = Tk()
window.title("Reservation")
window.geometry("800x800")
window.configure(cursor="hand2" , background="snow3")

img=Image.open("reservation.png")
img=img.resize((250 , 100))
img=ImageTk.PhotoImage(img)
my_label = Label(window, image=img)
my_label.place(x=20 , y=20)

Label(window , text="Reservation code").place(x=20 , y=150)
reservation_code=IntVar()
Entry(window, textvariable=reservation_code).place(x=150, y=150)

Label(window, text="Check in date").place(x=20, y=200)
check_in_date=StringVar()
Entry(window, textvariable=check_in_date).place(x=150, y=200)

Label(window, text="Nights").place(x=20, y=250)
nights=IntVar()
Entry(window, textvariable=nights).place(x=150, y=250)

Label(window, text="Payment status").place(x=20, y=300)
payment_status=StringVar(value="pending")
ttk.Combobox(window, textvariable=payment_status , values=payment_status_list , state="readonly").place(x=150, y=300)

Label(window, text="Room number").place(x=20, y=350)
room_number=IntVar()
Entry(window, textvariable=room_number).place(x=150, y=350)

Label(window, text="Guest name").place(x=20, y=400)
guest_name=StringVar()
Entry(window, textvariable=guest_name).place(x=150, y=400)


Label(window, text="Total price").place(x=20, y=450)
total_price=IntVar()
Entry(window, textvariable=total_price).place(x=150, y=450)


Label(window, text="Special requests").place(x=20, y=500)
special_requests=StringVar()
Entry(window, textvariable=special_requests).place(x=150, y=500)

Label(window, text="Cancelled ?").place(x=20, y=550)
cancelled=StringVar(value="No")
ttk.Combobox(window, textvariable=cancelled , values=is_cancelled_list , state="readonly ").place(x=150, y=550)

reservation_table=ttk.Treeview(window , columns=[1 , 2, 3 , 4 , 5, 6, 7 , 8, 9] , show="headings")
reservation_table.heading(1 , text="Reservation code")
reservation_table.heading(2 , text="Check in date")
reservation_table.heading(3 , text="Nights")
reservation_table.heading(4 , text="Payment status")
reservation_table.heading(5 , text="Room number")
reservation_table.heading(6 , text="Guest name")
reservation_table.heading(7 , text="Total price")
reservation_table.heading(8 , text="Special requests")
reservation_table.heading(9 , text="Cancelled ?")

reservation_table.column(1 , width=80 , anchor=CENTER)
reservation_table.column(2 , width=150 , anchor=CENTER)
reservation_table.column(3 , width=80 , anchor=CENTER)
reservation_table.column(4 , width=100 , anchor=CENTER)
reservation_table.column(5 , width=80 , anchor=CENTER)
reservation_table.column(6 , width=150 , anchor=CENTER)
reservation_table.column(7 , width=80 , anchor=CENTER)
reservation_table.column(8 , width=150 , anchor=CENTER)
reservation_table.column(9 , width=80 , anchor=CENTER)

reservation_table.place(x=350, y=150)

Button(window , text="Save" , width=18 , command=save_reservation).place(x=20, y=650)
Button(window , text= "Edit" , width=18 , command=edit_reservation).place(x=180, y=650)
Button(window , text="Delete" , width=18 , command=delete_reservation).place(x=20, y=680)
Button(window , text="Clear" , width=18 , command=reset_reservation).place(x=180, y=680)
Button(window , text="Search" , width=41 , command=search_reservation).place(x=20 , y=710)








window.mainloop()
