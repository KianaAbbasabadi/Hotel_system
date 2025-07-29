from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from controller.reservation_controller import ReservationController
from model.entity.reservation import Reservation
payment_status_list=["pending" , "paid" , "refunded" , "unpaid"]
is_cancelled_list=["Yes" , "No"]

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

Label(window, text="Guest number").place(x=20, y=400)
guest_number=StringVar()
Entry(window, textvariable=guest_number).place(x=150, y=400)


Label(window, text="Total price").place(x=20, y=450)
total_price=IntVar()
Entry(window, textvariable=total_price).place(x=150, y=450)


Label(window, text="Special requests").place(x=20, y=500)
special_requests=StringVar()
Entry(window, textvariable=special_requests).place(x=150, y=500)

Label(window, text="Cancelled ?").place(x=20, y=550)
cancelled=StringVar(value="No")
ttk.Combobox(window, textvariable=cancelled , values=is_cancelled_list , state="readonly ").place(x=150, y=550)








window.mainloop()
