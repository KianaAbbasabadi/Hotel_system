from model.entity.reservation import Reservation
from model.repository.reservation_repository import ReservationRepository



class ReservationController:
    def save(self, reservation_code, check_in_date , nights, payment_status,room_number, guest_name, total_price, special_requests, is_cancelled=False):
        try:
         reservation=Reservation( reservation_code, check_in_date , nights, payment_status, room_number, guest_name, total_price,special_requests, is_cancelled=False)
         reservation_repository=ReservationRepository()
         reservation_repository.save(reservation)
         return True , f"reservation saved {reservation}"
        except Exception as e:
            return False, f"Error saving reservation {e}"


    def edite(self,  reservation_code, check_in_date , nights, payment_status,room_number, guest_name, total_price, special_requests, is_cancelled=False):
        try:
            reservation = Reservation(reservation_code, check_in_date, nights, payment_status, room_number, guest_name,total_price, special_requests, is_cancelled=False)
            reservation_repository = ReservationRepository()
            reservation_repository.edite(reservation)
            return True , f"reservation edited {reservation}"
        except Exception as e:
            return False, f"Error editing reservation {e}"

    def delete(self, reservation_code):
        try:
            reservation_repository=ReservationRepository()
            reservation_repository.delete(reservation_code)
            return True , f"reservation deleted {reservation_code}"
        except Exception as e:
            return False, f"Error deleting reservation {e}"

    def find_all(self):
        try:
            reservation_repository=ReservationRepository()
            reservations=reservation_repository.find_all()
            return True, reservations
        except Exception as e:
            return False, f"Error finding reservations {e}"

    def find_by_code(self, reservation_code):
        try:
            reservation_repository=ReservationRepository()
            reservations=reservation_repository.find_by_code(reservation_code)
            return True, reservations
        except Exception as e:
            return False, f"Error finding reservations {e}"

    def find_by_guest_name(self, guest_name):
       try:
           reservation_repository=ReservationRepository()
           reservations=reservation_repository.find_by_guest_name(guest_name)
           return True, reservations
       except Exception as e:
           return False, f"Error finding reservations  {e}"

    def find_by_check_in_date(self, check_in_date):
        try:
            reservation_repository=ReservationRepository()
            reservations=reservation_repository.find_by_check_in_date(check_in_date)
            return True, reservations
        except Exception as e:
            return False, f"Error finding reservations check_in_date {e}"

    def find_by_nights(self, nights):
        try:
            reservation_repository=ReservationRepository()
            reservations=reservation_repository.find_by_nights(nights)
            return True, reservations
        except Exception as e:
            return False, f"Error finding reservations nights {e}"

    def find_by_payment_status(self, payment_status):
        try:
            reservation_repository=ReservationRepository()
            reservations=reservation_repository.find_by_payment_status(payment_status)
            return True, reservations
        except Exception as e:
            return False, f"Error finding reservations payment_status {e}"

    def find_by_room_number(self, room_number):
        try:
            reservation_repository=ReservationRepository()
            reservations=reservation_repository.find_by_room_number(room_number)
            return True, reservations
        except Exception as e:
            return False, f"Error finding reservations room_number {e}"

    def find_by_total_price(self, total_price):
        try:
            reservation_repository=ReservationRepository()
            reservations=reservation_repository.find_by_total_price(total_price)
            return True, reservations
        except Exception as e:
            return False, f"Error finding reservations total price {e}"

    def find_by_is_canceled(self, is_canceled):
        try:
            reservation_repository=ReservationRepository()
            reservation=reservation_repository.find_by_is_canceled(is_canceled)
            return True, reservation
        except Exception as e:
            return False, f"Error finding reservations {e}"