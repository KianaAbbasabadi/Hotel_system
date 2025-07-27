import sqlite3

from model.entity import guest


class GuestRepository:
    def connect(self):
        self.connection = sqlite3.connect('hotel_db.sqlite')
        self.cursor = self.connection.cursor()

    def disconnect(self , commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, guest):

            self.connect()
            self.cursor.execute(
                """insert into guests
                       (guest_code, name, family, age, phone_number, birth_date)
                   values (?, ?, ?, ?, ?, ?)""",
                [guest.guest_code, guest.name, guest.family, guest.age, guest.phone_number, guest.birth_date]
            )
            self.disconnect(commit=True)



    def edite(self, guest):
        self.connect()
        self.cursor.execute("update guests set name=?, family=?, age=?, phone_number=? , birth_date=?  where guest_code=?",
                       [guest.name , guest.family , guest.age , guest.phone_number, guest.birth_date , guest.guest_code])

        self.disconnect(commit=True)
    def delete(self, guest_code):
        self.connect()
        self.cursor.execute("delete from guests where guest_code= ?", [guest_code])
        self.disconnect(commit=True)

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from guests")
        guests_list = self.cursor.fetchall()

        self.disconnect()
        return guests_list
    def find_by_code(self, guest_code):
        self.connect()
        self.cursor.execute("select * from guests where guest_code= ?", [guest_code])
        guest_list = self.cursor.fetchone()
        self.disconnect()
        return guest_list

    def find_by_name_family(self, name , family):
        self.connect()
        self.cursor.execute("select * from guests where name = ? and family = ?;" , [name, family])
        guests_list = self.cursor.fetchall()
        self.disconnect()
        return guests_list
    def find_by_phone_number(self, phone_number):
        self.connect()
        self.cursor.execute("select * from guests where phone_number = ?", [phone_number])
        guests_list = self.cursor.fetchall()
        self.disconnect()
        return guests_list