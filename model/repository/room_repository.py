import sqlite3
from model.entity import room

class RoomRepository:
    def connect(self):
        self.connection = sqlite3.connect('hotel_db.sqlite')
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, room):
        self.connect()
        self.cursor.execute(
            """insert into rooms
                   (room_code, room_type, price_per_night, floor, is_booked, max_occupancy, has_balcony, view_type)
            values (?, ?, ?, ?, ?, ?, ?, ?)""",
            [room.room_code, room.room_type, room.price_per_night, room.floor, room.is_booked, room.max_occupancy, room.has_balcony, room.view_type]
        )
        self.disconnect(commit=True)

    def edited(self, room):
        self.connect()
        self.cursor.execute(
            "update rooms set room_type=?, price_per_night=?, floor=?, is_booked=?, max_occupancy=?, has_balcony=?, view_type=? where room_code=?",
            [room.room_type, room.price_per_night, room.floor, room.is_booked, room.max_occupancy, room.has_balcony, room.view_type, room.room_code]
        )
        self.disconnect(commit=True)

    def delete(self, room_code):
        self.connect()
        self.cursor.execute("delete from rooms where room_code=?", [room_code])
        self.disconnect(commit=True)

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from rooms")
        rooms_list = self.cursor.fetchall()
        self.disconnect()
        return rooms_list

    def find_by_code(self, room_code):
        self.connect()
        self.cursor.execute("select * from rooms where room_code=?", [room_code])
        room_data = self.cursor.fetchone()
        self.disconnect()
        return room_data

    def find_by_room_type(self, room_type):
        self.connect()
        self.cursor.execute("select * from rooms where room_type=?", [room_type])
        rooms_list = self.cursor.fetchall()
        self.disconnect()
        return rooms_list

    def find_by_price_per_night(self, price_per_night):
        self.connect()
        self.cursor.execute("select * from rooms where price_per_night=?", [price_per_night])
        rooms_list = self.cursor.fetchall()
        self.disconnect()
        return rooms_list

    def find_by_floor(self, floor):
        self.connect()
        self.cursor.execute("select * from rooms where floor=?", [floor])
        rooms_list = self.cursor.fetchall()
        self.disconnect()
        return rooms_list

    def find_by_is_booked(self, is_booked):
        self.connect()
        self.cursor.execute("select * from rooms where is_booked=?", [is_booked])
        rooms_list = self.cursor.fetchall()
        self.disconnect()
        return rooms_list

    def find_by_max_occupancy(self, max_occupancy):
        self.connect()
        self.cursor.execute("select * from rooms where max_occupancy=?", [max_occupancy])
        rooms_list = self.cursor.fetchall()
        self.disconnect()
        return rooms_list

    def find_by_has_balcony(self, has_balcony):
        self.connect()
        self.cursor.execute("select * from rooms where has_balcony=?", [has_balcony])
        rooms_list = self.cursor.fetchall()
        self.disconnect()
        return rooms_list

    def find_by_view_type(self, view_type):
        self.connect()
        self.cursor.execute("select * from rooms where view_type=?", [view_type])
        rooms_list = self.cursor.fetchall()
        self.disconnect()
        return rooms_list
