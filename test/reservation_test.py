from model.entity.reservation import Reservation
from model.repository.reservation_repository import ReservationRepository

#test passed
reservation_1 = Reservation(
    reservation_code=1,
    check_in_date="2023-12-15",
    nights=2,
    payment_status="Paid",
    room_number=101,
    guest_name="farnoosh abbasabadi",
    total_price=450000,
    special_requests="free mini bar",
    is_cancelled=0
)
reservation_2 = Reservation(
    reservation_code=2,
    check_in_date="2023-12-18",
    nights=5,
    payment_status="Paid",
    room_number=202,
    guest_name=" ali alippour",
    total_price=550000,
    special_requests="smoke free",
    is_cancelled=1
)
#test passed
#print(reservation_1)
#print(reservation_1.to_tuple())
#test passed
reservation_repo=ReservationRepository()
#reservation_repo.save(reservation_1)
#reservation_repo.save(reservation_2)
#test passed
#reservation_repo.edite(reservation_1)
#test passed
#reservation_repo.delete(1)
#test passed
#print(reservation_repo.find_all())
#test passed
#print(reservation_repo.find_by_code(2))
#test passed
#print(reservation_repo.find_by_guest_name("farnoosh abbasabadi"))
#test passed
#print(reservation_repo.find_by_check_in_date("2023-12-18"))
#test passed
#print(reservation_repo.find_by_nights(2))
#test passed
#print(reservation_repo.find_by_payment_status('Paid'))
#test passed
#print(reservation_repo.find_by_room_number(101))
#test passed
#print(reservation_repo.find_by_total_price(550000))
#test passed
#print(reservation_repo.find_by_is_canceled(0))
