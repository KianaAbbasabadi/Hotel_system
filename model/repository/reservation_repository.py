import sqlite3
from model.entity import reservation

class ReservationRepository:
    def save(self, reservation):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute(
            """insert into reservations
                   (reservation_code, guest_name, room_number, check_in_date, nights, payment_status)
            values (?, ?, ?, ?, ?, ?)""",
            [reservation.reservation_code, reservation.guest_name, reservation.room_number, reservation.check_in_date, reservation.nights, reservation.payment_status]
        )
        connection.commit()
        cursor.close()
        connection.close()

    def edited(self, reservation):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("update reservations set guest_name=?, room_number=?, check_in_date=?, nights=?, payment_status=? where reservation_code=?",
                       [reservation.guest_name, reservation.room_number, reservation.check_in_date, reservation.nights, reservation.payment_status, reservation.reservation_code])
        connection.commit()
        cursor.close()
        connection.close()

    def delete(self, reservation_code):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("delete from reservations where reservation_code= ?", [reservation_code])
        connection.commit()
        cursor.close()
        connection.close()

    def find_all(self):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("select * from reservations")
        reservations_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return reservations_list

    def find_by_code(self, reservation_code):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("select * from reservations where reservation_code= ?", [reservation_code])
        reservation_data = cursor.fetchone()
        cursor.close()
        connection.close()
        return reservation_data

    def find_by_guest_name(self, guest_name):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("select * from reservations where guest_name= ?", [guest_name])
        reservations_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return reservations_list

    def find_by_check_in_date(self, check_in_date):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("select * from reservations where check_in_date= ?", [check_in_date])
        reservations_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return reservations_list

    def find_by_nights(self, nights):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("select * from reservations where nights= ?", [nights])
        reservations_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return reservations_list

    def find_by_payment_status(self, payment_status):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("select * from reservations where payment_status= ?", [payment_status])
        reservations_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return reservations_list

    def find_by_room_number(self, room_number):
        connection = sqlite3.connect('hotel_db.sqlite')
        cursor = connection.cursor()
        cursor.execute("select * from reservations where room_number= ?", [room_number])
        reservations_list = cursor.fetchall()
        cursor.close()
        connection.close()
        return reservations_list
