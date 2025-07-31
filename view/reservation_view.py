from tkinter import *
import tkinter.ttk as ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from controller.reservation_controller import ReservationController

payment_status_list = ["pending", "paid", "refunded", "unpaid"]
is_cancelled_list = ["Yes", "No"]


class ReservationView:
    def __init__(self):
        self.reservation_controller = ReservationController()
        self.window = Tk()
        self.window.title("Reservation View")
        self.window.geometry("800x800")
        self.window.config(cursor="hand2", background="snow3")

        img = Image.open('reservation.png')
        img = img.resize((250, 100))
        self.img = ImageTk.PhotoImage(img)
        my_label = Label(self.window, image=self.img)
        my_label.place(x=20, y=20)

        Label(self.window, text="Reservation code" , background="snow3").place(x=20, y=150)
        self.reservation_code = IntVar()
        Entry(self.window, textvariable=self.reservation_code).place(x=150, y=150)

        Label(self.window, text="Check in date" , background="snow3").place(x=20, y=200)
        self.check_in_date = StringVar()
        Entry(self.window, textvariable=self.check_in_date).place(x=150, y=200)

        Label(self.window, text="Nights" , background="snow3").place(x=20, y=250)
        self.nights = IntVar()
        Entry(self.window, textvariable=self.nights).place(x=150, y=250)

        Label(self.window, text="Payment status" , background="snow3").place(x=20, y=300)
        self.payment_status = StringVar(value="pending")
        ttk.Combobox(self.window, textvariable=self.payment_status,
                     values=payment_status_list, state="readonly", width=17).place(x=150, y=300)

        Label(self.window, text="Room number" , background="snow3").place(x=20, y=350)
        self.room_number = IntVar()
        Entry(self.window, textvariable=self.room_number).place(x=150, y=350)

        Label(self.window, text="Guest name" , background="snow3").place(x=20, y=400)
        self.guest_name = StringVar()
        Entry(self.window, textvariable=self.guest_name).place(x=150, y=400)

        Label(self.window, text="Total price" , background="snow3").place(x=20, y=450)
        self.total_price = IntVar()
        Entry(self.window, textvariable=self.total_price).place(x=150, y=450)

        Label(self.window, text="Special requests" , background="snow3").place(x=20, y=500)
        self.special_requests = StringVar()
        Entry(self.window, textvariable=self.special_requests).place(x=150, y=500)

        Label(self.window, text="Cancelled?" , background="snow3").place(x=20, y=550)
        self.is_cancelled = StringVar(value="No")
        ttk.Combobox(self.window, textvariable=self.is_cancelled,
                     values=is_cancelled_list, state="readonly", width=17).place(x=150, y=550)

        self.reservation_table = ttk.Treeview(self.window,
                                              columns=[1, 2, 3, 4, 5, 6, 7, 8, 9],
                                              show="headings")
        self.reservation_table.heading(1, text="Reservation code")
        self.reservation_table.heading(2, text="Check in date")
        self.reservation_table.heading(3, text="Nights")
        self.reservation_table.heading(4, text="Payment status")
        self.reservation_table.heading(5, text="Room number")
        self.reservation_table.heading(6, text="Guest name")
        self.reservation_table.heading(7, text="Total price")
        self.reservation_table.heading(8, text="Special requests")
        self.reservation_table.heading(9, text="Cancelled?")

        self.reservation_table.column(1, width=100, anchor=CENTER)
        self.reservation_table.column(2, width=100, anchor=CENTER)
        self.reservation_table.column(3, width=80, anchor=CENTER)
        self.reservation_table.column(4, width=100, anchor=CENTER)
        self.reservation_table.column(5, width=80, anchor=CENTER)
        self.reservation_table.column(6, width=150, anchor=CENTER)
        self.reservation_table.column(7, width=80, anchor=CENTER)
        self.reservation_table.column(8, width=150, anchor=CENTER)
        self.reservation_table.column(9, width=80, anchor=CENTER)
        self.reservation_table.place(x=350, y=150)

        Button(self.window, text="Save", width=10, command=self.save_reservation).place(x=20, y=650)
        Button(self.window, text="Edit", width=10, command=self.edit_reservation).place(x=190, y=650)
        Button(self.window, text="Delete", width=10, command=self.delete_reservation).place(x=20, y=680)
        Button(self.window, text="Clear", width=10, command=self.reset_reservation).place(x=190, y=680)
        Button(self.window, text="Search", width=34, command=self.search_reservation).place(x=20, y=710)

        self.reservation_table.bind("<<TreeviewSelect>>", self.table_selected)
        self.load_reservation()
        self.window.mainloop()

    def save_reservation(self):
        status, message = self.reservation_controller.save(
            self.reservation_code.get(),
            self.check_in_date.get(),
            self.nights.get(),
            self.payment_status.get(),
            self.room_number.get(),
            self.guest_name.get(),
            self.total_price.get(),
            self.special_requests.get(),
            self.is_cancelled.get()
        )
        if status:
            messagebox.showinfo("Reservation Saved", message)
            self.load_reservation()
            self.reset_reservation()
        else:
            messagebox.showerror("Reservation Not Saved", message)

    def edit_reservation(self):
        status, message = self.reservation_controller.edite(
            self.reservation_code.get(),
            self.check_in_date.get(),
            self.nights.get(),
            self.payment_status.get(),
            self.room_number.get(),
            self.guest_name.get(),
            self.total_price.get(),
            self.special_requests.get(),
            self.is_cancelled.get()
        )
        if status:
            messagebox.showinfo("Reservation Edited", message)
            self.load_reservation()
            self.reset_reservation()
        else:
            messagebox.showerror("Reservation Not Edited", message)

    def delete_reservation(self):
        status, message = self.reservation_controller.delete(self.reservation_code.get())
        if status:
            messagebox.showinfo("Reservation Deleted", message)
            self.load_reservation()
            self.reset_reservation()
        else:
            messagebox.showerror("Reservation Not Deleted", "Enter the reservation code please.")

    def reset_reservation(self):
        self.reservation_code.set(0)
        self.check_in_date.set("")
        self.nights.set(0)
        self.payment_status.set("pending")
        self.room_number.set(0)
        self.guest_name.set("")
        self.total_price.set(0)
        self.special_requests.set("")
        self.is_cancelled.set("No")

    def load_reservation(self):
        status, result = self.reservation_controller.find_all()
        if status:
            for row in self.reservation_table.get_children():
                self.reservation_table.delete(row)
            for reservation in result:
                self.reservation_table.insert("", "end", values=reservation)
        else:
            messagebox.showerror("Reservations Not Found", result)

    def table_selected(self, event):
        selected_item = self.reservation_table.focus()
        if selected_item:
            reservation_data = self.reservation_table.item(selected_item)['values']
            if reservation_data:
                self.reservation_code.set(reservation_data[0])
                self.check_in_date.set(reservation_data[1])
                self.nights.set(reservation_data[2])
                self.payment_status.set(reservation_data[3])
                self.room_number.set(reservation_data[4])
                self.guest_name.set(reservation_data[5])
                self.total_price.set(reservation_data[6])
                self.special_requests.set(reservation_data[7])
                self.is_cancelled.set(reservation_data[8])

    def search_reservation(self):
        guest_name_value = self.guest_name.get()
        reservation_code_value = self.reservation_code.get()

        if guest_name_value or reservation_code_value:
            if reservation_code_value:
                status, result = self.reservation_controller.find_by_code(reservation_code_value)
            else:
                status, result = self.reservation_controller.find_by_guest_name(guest_name_value)

            if status:
                self.reservation_table.delete(*self.reservation_table.get_children())
                for reservation in result:
                    self.reservation_table.insert("", "end", values=reservation)
            else:
                messagebox.showerror("Reservation Not Found", result)
        else:
            messagebox.showwarning("Input Error", "Please enter a guest name or reservation code to search.")





