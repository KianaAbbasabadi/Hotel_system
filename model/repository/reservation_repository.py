import sqlite3
from model.entity.reservation import Reservation

class ReservationRepository:
    def connect(self):
        self.connection = sqlite3.connect("./model/repository/hotel_db.sqlite")
        self.cursor = self.connection.cursor()

    def disconnect(self, commit=False):
        if commit:
            self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def save(self, reservation):
        try:
            self.connect()
            self.cursor.execute(
                """insert into reservations
                   (reservation_code, guest_name, room_number, check_in_date, nights, payment_status, total_price, special_requests, is_canceled)
                   values (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                [reservation.reservation_code, reservation.guest_name, reservation.room_number,
                 reservation.check_in_date, reservation.nights, reservation.payment_status,
                 reservation.total_price, reservation.special_requests, reservation.is_cancelled]
            )
            self.disconnect(commit=True)
        except Exception as e:
            print(f"Error occurred: {e}")
            self.disconnect()

    def edite(self, reservation):
        self.connect()
        self.cursor.execute(
            """update reservations set guest_name=?, room_number=?, check_in_date=?, nights=?, payment_status=?, total_price=?, special_requests=?, is_canceled=?
               where reservation_code=?""",
            [reservation.guest_name, reservation.room_number, reservation.check_in_date, reservation.nights,
             reservation.payment_status, reservation.total_price, reservation.special_requests, reservation.is_cancelled,
             reservation.reservation_code]
        )
        self.disconnect(commit=True)

    def delete(self, reservation_code):
        self.connect()
        self.cursor.execute("delete from reservations where reservation_code=?", [reservation_code])
        self.disconnect(commit=True)

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from reservations")
        reservations_list = self.cursor.fetchall()
        self.disconnect()
        return reservations_list

    def find_by_code(self, reservation_code):
        self.connect()
        self.cursor.execute("select * from reservations where reservation_code=?", [reservation_code])
        reservation_data = self.cursor.fetchone()
        self.disconnect()
        return reservation_data

    def find_by_guest_name(self, guest_name):
        self.connect()
        self.cursor.execute("select * from reservations where guest_name=?", [guest_name])
        reservations_list = self.cursor.fetchall()
        self.disconnect()
        return reservations_list

    def find_by_check_in_date(self, check_in_date):
        self.connect()
        self.cursor.execute("select * from reservations where check_in_date=?", [check_in_date])
        reservations_list = self.cursor.fetchall()
        self.disconnect()
        return reservations_list

    def find_by_nights(self, nights):
        self.connect()
        self.cursor.execute("select * from reservations where nights=?", [nights])
        reservations_list = self.cursor.fetchall()
        self.disconnect()
        return reservations_list

    def find_by_payment_status(self, payment_status):
        self.connect()
        self.cursor.execute("select * from reservations where payment_status=?", [payment_status])
        reservations_list = self.cursor.fetchall()
        self.disconnect()
        return reservations_list

    def find_by_room_number(self, room_number):
        self.connect()
        self.cursor.execute("select * from reservations where room_number=?", [room_number])
        reservations_list = self.cursor.fetchall()
        self.disconnect()
        return reservations_list
    def find_by_total_price(self, total_price):
        self.connect()
        self.cursor.execute("select * from reservations where total_price=?", [total_price])
        reservations_list = self.cursor.fetchall()
        self.disconnect()
        return reservations_list

    def find_by_is_canceled(self, is_canceled):
        self.connect()
        self.cursor.execute("select * from reservations where is_canceled=?", [is_canceled])
        reservations_list = self.cursor.fetchall()
        self.disconnect()
        return reservations_list


