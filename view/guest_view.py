from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from controller.guest_controller import GuestController
from model.entity.guest import Guest


class GuestView:
    def __init__(self , parent):
        self.guest_controller = GuestController()
        self.window = Toplevel(parent)
        self.window.title("Guest View")
        self.window.geometry("800x800")
        self.window.config(cursor="hand2", background="snow3")

        img = Image.open('guest.png')
        img = img.resize((250, 100))
        self.img = ImageTk.PhotoImage(img)
        my_label = Label(self.window, image=self.img)
        my_label.place(x=20, y=20)

        Label(self.window, text="Guest code", background="snow3").place(x=20, y=150)
        self.guest_code = IntVar()
        Entry(self.window, textvariable=self.guest_code).place(x=150, y=150)

        Label(self.window, text="Name", background="snow3").place(x=20, y=200)
        self.name = StringVar()
        Entry(self.window, textvariable=self.name).place(x=150, y=200)

        Label(self.window, text="Family", background="snow3").place(x=20, y=250)
        self.family = StringVar()
        Entry(self.window, textvariable=self.family).place(x=150, y=250)

        Label(self.window, text="Age", background="snow3").place(x=20, y=300)
        self.age = IntVar()
        Entry(self.window, textvariable=self.age).place(x=150, y=300)

        Label(self.window, text="Phone number", background="snow3").place(x=20, y=350)
        self.phone_number = StringVar()
        Entry(self.window, textvariable=self.phone_number).place(x=150, y=350)

        Label(self.window, text="Birth date", background="snow3").place(x=20, y=400)
        self.birth_date = StringVar()
        Entry(self.window, textvariable=self.birth_date).place(x=150, y=400)

        self.guest_table = ttk.Treeview(self.window, columns=[1, 2, 3, 4, 5, 6], show="headings")
        self.guest_table.heading(1, text="Guest Code")
        self.guest_table.heading(2, text="Name")
        self.guest_table.heading(3, text="Family")
        self.guest_table.heading(4, text="Age")
        self.guest_table.heading(5, text="Phone number")
        self.guest_table.heading(6, text="Birth date")

        self.guest_table.column(1, width=100, anchor=CENTER)
        self.guest_table.column(2, width=150, anchor=CENTER)
        self.guest_table.column(3, width=150, anchor=CENTER)
        self.guest_table.column(4, width=150, anchor=CENTER)
        self.guest_table.column(5, width=150, anchor=CENTER)
        self.guest_table.column(6, width=150, anchor=CENTER)
        self.guest_table.place(x=350, y=150 )


        Button(self.window, text="Save", width=10, command=self.save_guest).place(x=20, y=550)
        Button(self.window, text="Edit", width=10, command=self.edit_guest).place(x=190, y=550)
        Button(self.window, text="Delete", width=10, command=self.delete_guest).place(x=20, y=580)
        Button(self.window, text="Clear", width=10, command=self.reset_guest).place(x=190, y=580)
        Button(self.window, text="Search", width=34, command=self.search_guest).place(x=20, y=610)

        self.guest_table.bind("<<TreeviewSelect>>", self.table_selected)
        self.window.mainloop()

    def save_guest(self):
        status, message = self.guest_controller.save(
            self.guest_code.get(),
            self.name.get(),
            self.family.get(),
            self.age.get(),
            self.phone_number.get(),
            self.birth_date.get()
        )
        if status:
            messagebox.showinfo("Guest Saved", message)
            self.load_guest()
            self.reset_guest()
        else:
            messagebox.showerror("Guest Not Saved", message)

    def edit_guest(self):
        status, message = self.guest_controller.edite(
            self.guest_code.get(),
            self.name.get(),
            self.family.get(),
            self.age.get(),
            self.phone_number.get(),
            self.birth_date.get()
        )
        if status:
            messagebox.showinfo("Guest Edited", message)
            self.load_guest()
            self.reset_guest()
        else:
            messagebox.showerror("Guest Not Edited", message)

    def delete_guest(self):
        status, message = self.guest_controller.delete(self.guest_code.get())
        if status:
            messagebox.showinfo("Guest Deleted", message)
            self.load_guest()
            self.reset_guest()
        else:
            messagebox.showerror("Guest Not Deleted", "Enter the guest code please.")

    def reset_guest(self):
        self.guest_code.set(0)
        self.name.set("")
        self.family.set("")
        self.age.set("")
        self.phone_number.set("")
        self.birth_date.set("")

    def load_guest(self):
        status, result = self.guest_controller.find_all()
        if status:
            for row in self.guest_table.get_children():
                self.guest_table.delete(row)
            for guest in result:
                self.guest_table.insert("", "end", values=guest)
        else:
            messagebox.showerror("Guests Not Found", result)

    def table_selected(self, event):
        selected_item = self.guest_table.focus()
        if selected_item:
            guest_data = self.guest_table.item(selected_item)['values']
            if guest_data:
                self.guest_code.set(guest_data[0])
                self.name.set(guest_data[1])
                self.family.set(guest_data[2])
                self.age.set(guest_data[3])
                self.phone_number.set(guest_data[4])
                self.birth_date.set(guest_data[5])

    def search_guest(self):
        name_value = self.name.get()
        family_value = self.family.get()

        if name_value or family_value:
            status, result = self.guest_controller.find_by_name_family(name_value, family_value)
            if status:
                self.guest_table.delete(*self.guest_table.get_children())
                for guest in result:
                    self.guest_table.insert("", "end", values=guest)
            else:
                messagebox.showerror("Guest Not Found", result)
        else:
            messagebox.showwarning("Input Error", "Please enter a name or family to search.")










