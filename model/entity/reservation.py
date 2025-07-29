from model.tool.validation import *


class Reservation:
    def __init__(self, reservation_code, check_in_date, nights, payment_status,
                 room_number, guest_name, total_price,
                 special_requests, is_cancelled):

        self.reservation_code = reservation_code
        self.check_in_date = check_in_date
        self.nights = nights
        self.payment_status = payment_status
        self.room_number = room_number
        self.guest_name = guest_name
        self.total_price = total_price
        self.special_requests = special_requests
        self.is_cancelled = is_cancelled

    def __str__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return (self.reservation_code, self.check_in_date, self.nights,
                self.payment_status, self.room_number, self.guest_name,
                self.total_price, self.special_requests, self.is_cancelled)

    @property
    def reservation_code(self):
        return self._reservation_code

    @reservation_code.setter
    def reservation_code(self, value):
        reservation_code_validator(value)
        self._reservation_code = value

    @property
    def check_in_date(self):
        return self._check_in_date

    @check_in_date.setter
    def check_in_date(self, value):
        check_in_date_validator(value)
        self._check_in_date = value

    @property
    def nights(self):
        return self._nights

    @nights.setter
    def nights(self, value):
        nights_validator(value)
        self._nights = value

    @property
    def payment_status(self):
        return self._payment_status

    @payment_status.setter
    def payment_status(self, value):

        self._payment_status = value

    @property
    def room_number(self):
        return self._room_number

    @room_number.setter
    def room_number(self, value):
       room_number_validator(value)
       self._room_number = value

    @property
    def guest_name(self):
        return self._guest_name

    @guest_name.setter
    def guest_name(self, value):
        guest_name_validator(value)
        self._guest_name = value

    @property
    def total_price(self):
        return self._total_price

    @total_price.setter
    def total_price(self, value):
        total_price_validator(value)
        self._total_price = value

    @property
    def special_requests(self):
        return self._special_requests

    @special_requests.setter
    def special_requests(self, value):
        special_requests_validator(value)
        self._special_requests = value

    @property
    def is_cancelled(self):
        return self._is_cancelled

    @is_cancelled.setter
    def is_cancelled(self, value):
        self._is_cancelled = value
