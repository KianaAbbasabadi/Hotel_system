import sqlite3

from model.entity import guest


class GuestRepository:
    def save(self, guest):
     connection = sqlite3.connect('hotel_db.sqlite')
     cursor = connection.cursor()
     cursor.execute(
         """insert into guests
                (guest_code ,name,family,age, phone_number, birth_date )
         values (?, ?, ?, ?, ? , ?)""",
         [guest.guest_code, guest.name, guest.family, guest.age, guest.phone_number, guest.birth_date]
     )
     connection.commit()
     cursor.close()
     connection.close()

    def edited(self, guest):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("update guests set name=?, family=?, age=?, phone_number=? , birth_date=?  where guest_code=?",
                       [guest.name , guest.family , guest.age , guest.phone_number, guest.birth_date , guest.guest_code])
        connection.commit()
        cursor.close()
        connection.close()

    def delete(self, code):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("delete from guests where guest_code= ?", [guest.guest_code])
        connection.commit()
        cursor.close()
        connection.close()

    def find_all(self):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("select * from guests")
        guests_list = cursor.fetchall()

        cursor.close()
        connection.close()
        return guests_list
    def find_by_code(self, guest_code):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("select * from guests where guest_code= ?", [guest_code])
        guest_list = cursor.fetchone()
        cursor.close()
        connection.close()
        return guest_list

    def find_by_name_family(self, name , family):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("select * from guests where name = ? and family = ?;" , [name, family])
        guests_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return guests_list
    def find_by_phone_number(self, phone_number):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("select * from guests where phone_number = ?", [phone_number])
        guests_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return guests_list