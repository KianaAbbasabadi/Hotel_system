import re
from datetime import datetime

def guest_code_validator(guest_code):
    if not (type(guest_code) == int and guest_code > 0):
        raise ValueError("Guest code must be a positive integer")


def name_validator(name):
    if not (type(name) == str and re.match(r"^[A-Za-z\s]{3,30}$", name)):
        raise ValueError("Name is invalid")


def family_validator(family):
    if not (type(family) == str and re.match(r"^[A-Za-z\s]{3,40}$", family)):
        raise ValueError("Family is invalid")


def age_validator(age):
    if not (type(age) == int and 0 <= age <= 100):
        raise ValueError("Age must be an integer between 0 and 100")


def phone_number_validator(phone_number):
    if not (type(phone_number) == str and re.match(r"^09\d{9}$", phone_number)):
        raise ValueError("Phone number must start with '09' and have exactly 11 digits")


def birth_date_validator(birth_date):
    try:
        if type(birth_date) == str:
            datetime.strptime(birth_date, "%Y-%m-%d")
        elif type(birth_date) == datetime:
            pass
    except Exception as e:
        print(f"{e} not a valid date")


def reservation_code_validator(reservation_code):
    if not (type(reservation_code) == int and reservation_code > 0):
        raise ValueError("Reservation code must be a positive integer")


def check_in_date_validator(check_in_date):
    try:
        if type(check_in_date) == str:
            datetime.strptime(check_in_date, "%Y-%m-%d")
        elif type(check_in_date) == datetime:
            pass
        else:
            raise ValueError()
    except Exception:
        raise ValueError("Check-in date must be in YYYY-MM-DD format or datetime object")


def nights_validator(nights):
    if not (type(nights) == int and 1 <= nights <= 30):
        raise ValueError("Nights must be integer between 1 and 30")


def room_number_validator(room_number):
    if not (type(room_number) == int and 100 < room_number < 700):
        raise ValueError("Room number is invalid")


def guest_name_validator(guest_name):
    if not (type(guest_name) == str and re.match(r"^[A-Za-z\s]{3,30}$", guest_name)):
        raise ValueError("Guest name is invalid")


def total_price_validator(total_price):
    if not (type(total_price) == int and total_price > 0):
        raise ValueError("Total price is invalid")


def special_requests_validator(special_requests):
    if not (type(special_requests) == str):
        raise ValueError("Special requests are invalid")


def room_code_validator(room_code):
    if not (type(room_code) == int and room_code > 0):
        raise ValueError("Room code must be a positive integer")


def price_per_night_validator(price_per_night):
    if not (type(price_per_night) == int and price_per_night > 0):
        raise ValueError("Price per night is invalid")


def max_occupancy_validator(max_occupancy):
    if not (type(max_occupancy) == int and 0 < max_occupancy < 7):
        raise ValueError("Max occupancy is invalid")














