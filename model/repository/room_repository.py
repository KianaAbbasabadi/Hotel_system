import sqlite3
from model.entity import room

class RoomRepository:
    def save(self, room):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute(
            """insert into rooms
                   (room_code, room_type, price_per_night, floor, is_booked, max_occupancy, has_balcony, view_type)
            values (?, ?, ?, ?, ?, ?, ?, ?)""",
            [room.room_code, room.room_type, room.price_per_night, room.floor, room.is_booked, room.max_occupancy, room.has_balcony, room.view_type]
        )
        connection.commit()
        cursor.close()
        connection.close()

    def edited(self, room):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("update rooms set room_type=?, price_per_night=?, floor=?, is_booked=?, max_occupancy=?, has_balcony=?, view_type=? where room_code=?",
                       [room.room_type, room.price_per_night, room.floor, room.is_booked, room.max_occupancy, room.has_balcony, room.view_type, room.room_code])
        connection.commit()
        cursor.close()
        connection.close()

    def delete(self, room_code):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("delete from rooms where room_code= ?", [room_code])
        connection.commit()
        cursor.close()
        connection.close()

    def find_all(self):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("select * from rooms")
        rooms_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return rooms_list

    def find_by_code(self, room_code):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("select * from rooms where room_code= ?", [room_code])
        room_data = cursor.fetchone()
        cursor.close()
        connection.close()
        return room_data

    def find_by_room_type(self, room_type):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("select * from rooms where room_type= ?", [room_type])
        rooms_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return rooms_list

    def find_by_price_per_night(self, price_per_night):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("select * from rooms where price_per_night= ?", [price_per_night])
        rooms_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return rooms_list

    def find_by_floor(self, floor):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("select * from rooms where floor= ?", [floor])
        rooms_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return rooms_list

    def find_by_is_booked(self, is_booked):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("select * from rooms where is_booked= ?", [is_booked])
        rooms_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return rooms_list

    def find_by_max_occupancy(self, max_occupancy):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("select * from rooms where max_occupancy= ?", [max_occupancy])
        rooms_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return rooms_list

    def find_by_has_balcony(self, has_balcony):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("select * from rooms where has_balcony= ?", [has_balcony])
        rooms_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return rooms_list

    def find_by_view_type(self, view_type):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("select * from rooms where view_type= ?", [view_type])
        rooms_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return rooms_list
