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


    def edite(self, reservation):
        pass

    def delete(self, reservation_code):
        pass

    def find_all(self):
        pass

    def find_by_code(self, reservation_code):
        pass

    def find_by_guest_name(self, guest_name):
        pass

    def find_by_check_in_date(self, check_in_date):
        pass

    def find_by_nights(self, nights):
        pass

    def find_by_payment_status(self, payment_status):
        pass

    def find_by_room_number(self, room_number):
        pass

    def find_by_total_price(self, total_price):
        pass

    def find_by_is_canceled(self, is_canceled):
        pass