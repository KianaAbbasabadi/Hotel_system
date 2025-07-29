from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from controller.room_controller import RoomController

room_type_list = ["Standard", "Delux", "Suite", "Family"]
view_type_list = ["City", "Sea", "Garden", "Pool", "None"]
floor_list = [1, 2, 3, 4, 5, 6]

class RoomView:
    def __init__(self):
        self.room_controller = RoomController()
        self.window = Tk()
        self.window.title("Room View")
        self.window.geometry("800x800")
        self.window.config(cursor="hand2", background="snow3")

        img = Image.open('room.png')
        img = img.resize((250, 100))
        self.img = ImageTk.PhotoImage(img)
        my_label = Label(self.window, image=self.img)
        my_label.place(x=20, y=20)

        Label(self.window, text="Room code").place(x=20, y=150)
        self.room_code = IntVar()
        Entry(self.window, textvariable=self.room_code).place(x=150, y=150)

        Label(self.window, text="Room type").place(x=20, y=200)
        self.room_type = StringVar(value=room_type_list[0])
        ttk.Combobox(self.window, textvariable=self.room_type, values=room_type_list, state="readonly").place(x=150, y=200)

        Label(self.window, text="Price per night").place(x=20, y=250)
        self.price_per_night = IntVar()
        Entry(self.window, textvariable=self.price_per_night).place(x=150, y=250)

        Label(self.window, text="Floor").place(x=20, y=300)
        self.floor = StringVar(value=floor_list[0])
        ttk.Combobox(self.window, textvariable=self.floor, values=floor_list, state="readonly").place(x=150, y=300)

        Label(self.window, text="Booked?").place(x=20, y=350)
        self.is_booked = StringVar(value="No")
        ttk.Combobox(self.window, textvariable=self.is_booked, values=["Yes", "No"], state="readonly").place(x=150, y=350)

        Label(self.window, text="Max occupancy").place(x=20, y=400)
        self.max_occupancy = IntVar()
        Entry(self.window, textvariable=self.max_occupancy).place(x=150, y=400)

        Label(self.window, text="Has balcony?").place(x=20, y=450)
        self.has_balcony = StringVar(value="Yes")
        ttk.Combobox(self.window, textvariable=self.has_balcony, values=["Yes", "No"], state="readonly").place(x=150, y=450)

        Label(self.window, text="View type").place(x=20, y=500)
        self.view_type = StringVar(value=view_type_list[0])
        ttk.Combobox(self.window, textvariable=self.view_type, values=view_type_list, state="readonly").place(x=150, y=500)

        self.room_table = ttk.Treeview(self.window, columns=[1, 2, 3, 4, 5, 6, 7, 8], show="headings")
        self.room_table.heading(1, text="Room code")
        self.room_table.heading(2, text="Room type")
        self.room_table.heading(3, text="Price per night")
        self.room_table.heading(4, text="Floor")
        self.room_table.heading(5, text="Booked?")
        self.room_table.heading(6, text="Max occupancy")
        self.room_table.heading(7, text="Has balcony?")
        self.room_table.heading(8, text="View type")

        self.room_table.column(1, width=80, anchor=CENTER)
        self.room_table.column(2, width=100, anchor=CENTER)
        self.room_table.column(3, width=100, anchor=CENTER)
        self.room_table.column(4, width=80, anchor=CENTER)
        self.room_table.column(5, width=100, anchor=CENTER)
        self.room_table.column(6, width=80, anchor=CENTER)
        self.room_table.column(7, width=100, anchor=CENTER)
        self.room_table.column(8, width=100, anchor=CENTER)

        self.room_table.place(x=350, y=150)

        Button(self.window, text="Save", width=18, command=self.save_room).place(x=20, y=650)
        Button(self.window, text="Edit", width=18, command=self.edit_room).place(x=180, y=650)
        Button(self.window, text="Delete", width=18, command=self.delete_room).place(x=20, y=680)
        Button(self.window, text="Clear", width=18, command=self.reset_room).place(x=180, y=680)
        Button(self.window, text="Search", width=41, command=self.search_room).place(x=20, y=710)

        self.room_table.bind("<<TreeviewSelect>>", self.table_select_room)
        self.load_room()
        self.window.mainloop()

    def save_room(self):
        status, message = self.room_controller.save(
            self.room_code.get(),
            self.room_type.get(),
            self.price_per_night.get(),
            self.floor.get(),
            self.is_booked.get(),
            self.max_occupancy.get(),
            self.has_balcony.get(),
            self.view_type.get()
        )
        if status:
            messagebox.showinfo("Room Saved", message)
            self.load_room()
            self.reset_room()
        else:
            messagebox.showerror("Room Not Saved", message)

    def edit_room(self):
        status, message = self.room_controller.edit(
            self.room_code.get(),
            self.room_type.get(),
            self.price_per_night.get(),
            self.floor.get(),
            self.is_booked.get(),
            self.max_occupancy.get(),
            self.has_balcony.get(),
            self.view_type.get()
        )
        if status:
            messagebox.showinfo("Room Edited", message)
            self.load_room()
            self.reset_room()
        else:
            messagebox.showerror("Room Not Edited", message)

    def delete_room(self):
        status, message = self.room_controller.delete(self.room_code.get())
        if status:
            messagebox.showinfo("Room Deleted", message)
            self.load_room()
            self.reset_room()
        else:
            messagebox.showerror("Room Not Deleted", "Enter the room code please.")

    def reset_room(self):
        self.room_code.set(0)
        self.room_type.set(room_type_list[0])
        self.price_per_night.set(0)
        self.floor.set(floor_list[0])
        self.is_booked.set("No")
        self.max_occupancy.set(0)
        self.has_balcony.set("Yes")
        self.view_type.set(view_type_list[0])

    def load_room(self):
        status, result = self.room_controller.find_all()
        if status:
            for row in self.room_table.get_children():
                self.room_table.delete(row)
            for room in result:
                self.room_table.insert("", "end", values=room)
        else:
            messagebox.showerror("Rooms Not Found", result)

    def table_select_room(self, event):
        selected_item = self.room_table.focus()
        if selected_item:
            room_data = self.room_table.item(selected_item)['values']
            if room_data:
                self.room_code.set(room_data[0])
                self.room_type.set(room_data[1])
                self.price_per_night.set(room_data[2])
                self.floor.set(room_data[3])
                self.is_booked.set(room_data[4])
                self.max_occupancy.set(room_data[5])
                self.has_balcony.set(room_data[6])
                self.view_type.set(room_data[7])

    def search_room(self):
        room_code_value = self.room_code.get()
        room_type_value = self.room_type.get()

        if room_code_value or room_type_value:
            if room_code_value:
                status, result = self.room_controller.find_by_code(room_code_value)
            else:
                status, result = self.room_controller.find_by_room_type(room_type_value)

            if status:
                self.room_table.delete(*self.room_table.get_children())
                for room in result:
                    self.room_table.insert("", "end", values=room)
            else:
                messagebox.showerror("Room Not Found", result)
        else:
            messagebox.showwarning("Input Error", "Please enter a room code or room type to search.")

