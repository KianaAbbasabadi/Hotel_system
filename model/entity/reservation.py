class Reservation:
    def __init__(self, reservation_code , check_in_date , nights , payment_status):
        self.reservation_code = reservation_code
        self.check_in_date = check_in_date
        self.nights = nights
        self.payment_status = payment_status


    def __str__(self):
        return f"{self.__dict__}"



    #todo:getter/setter -->validation