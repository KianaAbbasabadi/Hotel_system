from model.entity.reservation import Reservation
#test passed
reservation_1 = Reservation(
    reservation_code="R123",
    check_in_date="2023-12-15",
    nights=3,
    payment_status="Paid",
    room_number=101,
    guest_name="محمد رضایی",
    total_price=4500000,
    special_requests="نیاز به اتاق سیگار ممنوع",
    is_cancelled=False
)

print(reservation_1)
print(reservation_1.to_tuple())