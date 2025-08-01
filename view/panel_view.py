from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from tkinter import messagebox


from guest_app import *
from reservation_app import *
from room_app import *

class PanelView:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("600x600")
        self.window.title("Hotel System")
        self.window.config(cursor="hand2", background="snow3")

        self._create_widgets()

        self.window.mainloop()

    def _create_widgets(self):

        title_label = Label(self.window, text="Hotel System", font=("Arial", 30, "bold"), background="snow3")
        title_label.place(x=20, y=20)


        room_button = Button(self.window, text="Room management", command=self._open_room_management, width=20)
        room_button.place(x=20, y=100)

        guest_button = Button(self.window, text="Guest management", command=self._open_guest_management, width=20)
        guest_button.place(x=20, y=243)

        reservation_button = Button(self.window, text="Reservation management", command=self._open_reservation_management, width=20)
        reservation_button.place(x=20, y=385)



        img = Image.open("hotel.png")
        img = img.resize((300, 300))
        self.photo_img = ImageTk.PhotoImage(img)
        image_label = Label(self.window, image=self.photo_img)
        image_label.image = self.photo_img
        image_label.place(x=300, y=100)

    def _open_room_management(self):

        try:
            RoomView(self.window)
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Room Management: {e}")

    def _open_guest_management(self):

        try:
            GuestView(self.window)
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Guest Management: {e}")

    def _open_reservation_management(self):

        try:
            ReservationView(self.window)
        except Exception as e:
            messagebox.showerror("Error", f"Could not open Reservation Management: {e}")


