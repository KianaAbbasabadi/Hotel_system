from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from controller.room_controller import RoomController
room_type_list=["Standard" , "Delux" , "Suite" , "Family"]
view_type_list=["City" , "Sea"  , "Garden " , "Pool" , "None"]
floor_list=[1 , 2, 3 , 4 , 5 , 6]

def save_room():
    pass
def edit_room():
    pass
def delete_room():
    pass
def reset_room():
    pass
def load_room():
    pass
def table_select_room():
    pass
def search_room():
    pass

window = Tk()
window.title("Room View")
window.geometry("800x800")
window.config(cursor="hand2", background="snow3")

img = Image.open('room.png')
img=img.resize((250,100))
img = ImageTk.PhotoImage(img)
my_label = Label(window, image=img)
my_label.place(x=20 , y=20)

Label(window , text="Room code").place(x=20 , y=150)
room_code=IntVar()
Entry(window, textvariable=room_code).place(x=150, y=150)

Label(window, text="Room type").place(x=20, y=200)
room_type=StringVar(value=room_type_list[0])
ttk.Combobox(window, textvariable=room_type , values=room_type_list , state="readonly").place(x=150, y=200)

Label(window, text="Price per night").place(x=20, y=250)
price_per_night=IntVar()
Entry(window, textvariable=price_per_night).place(x=150, y=250)

Label(window, text="Floor").place(x=20, y=300)
floor=StringVar(value=floor_list[0])
ttk.Combobox(window, textvariable=floor , values=floor_list , state="readonly").place(x=150, y=300)

Label(window, text="Booked?").place(x=20, y=350)
is_booked=StringVar(value="No")
ttk.Combobox(window , textvariable=is_booked , values=["Yes", "No"] , state="readonly").place(x=150, y=350)

Label(window, text="Max occupancy").place(x=20, y=400)
max_occupancy=IntVar()
Entry(window, textvariable=max_occupancy ).place(x=150, y=400)

Label(window, text="Has balcony?").place(x=20, y=450)
has_balcony=StringVar(value="Yes")
ttk.Combobox(window , textvariable=has_balcony , values=["Yes", "No"] , state="readonly").place(x=150, y=450)

Label(window, text="View type").place(x=20, y=500)
view_type=StringVar(value=view_type_list[0])
ttk.Combobox(window , textvariable=view_type , values=view_type_list , state="readonly").place(x=150, y=500)

room_table=ttk.Treeview(window , columns=[1 , 2, 3, 4 , 5 , 6 , 7 , 8] , show="headings")
room_table.heading(1, text="Room code")
room_table.heading(2, text="Room type")
room_table.heading(3, text="Price per night")
room_table.heading(4, text="Floor")
room_table.heading(5, text="Booked?")
room_table.heading(6, text="Max occupancy")
room_table.heading(7, text="Has balcony?")
room_table.heading(8, text="View type")

room_table.column(1 , width=80 , anchor=CENTER)
room_table.column(2, width=100 , anchor=CENTER)
room_table.column(3, width=100 , anchor=CENTER)
room_table.column(4, width=80 , anchor=CENTER)
room_table.column(5, width=100 , anchor=CENTER)
room_table.column(6, width=80 , anchor=CENTER)
room_table.column(7, width=100 , anchor=CENTER)
room_table.column(8, width=100 , anchor=CENTER)

room_table.place(x=350 , y=150)

Button(window , text="Save" , width=18 , command=save_room).place(x=20 , y=650)
Button(window , text="Edit" , width=18 , command=edit_room).place(x=180, y=650)
Button(window , text="Delete" , width=18 , command=delete_room).place(x=20, y=680)
Button(window , text="Clear" , width=18 , command=reset_room).place(x=180, y=680)
Button(window , text="Search" , width=41 , command=search_room).place(x=20, y=710)









window.mainloop()