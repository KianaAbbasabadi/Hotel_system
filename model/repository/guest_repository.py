import sqlite3

class GuestRepository:
    def save(self, guest):
     connection = sqlite3.connect('hotel_db.sqlite')
     cursor = connection.cursor()
     cursor.execute("sql" , [data])
     connection.commit()
     cursor.close()
     connection.close()
    def edited(self, guest):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("sql", [data])
        connection.commit()
        cursor.close()
        connection.close()
    def delete(self, code):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("sql", [data])
        connection.commit()
        cursor.close()
        connection.close()
    def find_all(self):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("sql", [data])

        cursor.close()
        connection.close()
    def find_by_code(self, code):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("sql", [data])

        cursor.close()
        connection.close()
    def find_by_name_family(self, name , family):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("sql", [data])

        cursor.close()
        connection.close()
    def find_by_phone_number(self, phone_number):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("sql", [data])

        cursor.close()
        connection.close()