class Reservation:
    def __init__(self, reservation_code, check_in_date, nights, payment_status,
                 room_number, guest_name, total_price,
                 special_requests, is_cancelled=False):

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

    #todo:getter/setter -->validation