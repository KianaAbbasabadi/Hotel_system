from model.tool.validation import *


class Room:
    def __init__(self, room_code, room_type, price_per_night, floor,
                 is_booked, max_occupancy, has_balcony, view_type):
        self.room_code = room_code
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.floor = floor
        self.is_booked = is_booked
        self.max_occupancy = max_occupancy
        self.has_balcony = has_balcony
        self.view_type = view_type

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return (self.room_code, self.room_type, self.price_per_night, self.floor,
                self.is_booked, self.max_occupancy, self.has_balcony, self.view_type)

    @property
    def room_code(self):
        return self._room_code

    @room_code.setter
    def room_code(self, value):
        room_code_validator(value)
        self._room_code = value

    @property
    def room_type(self):
        return self._room_type

    @room_type.setter
    def room_type(self, value):
        self._room_type = value

    @property
    def price_per_night(self):
        return self._price_per_night

    @price_per_night.setter
    def price_per_night(self, value):
        price_per_night_validator(value)
        self._price_per_night = value

    @property
    def floor(self):
        return self._floor

    @floor.setter
    def floor(self, value):
        self._floor = value

    @property
    def is_booked(self):
        return self._is_booked

    @is_booked.setter
    def is_booked(self, value):
        self._is_booked = value

    @property
    def max_occupancy(self):
        return self._max_occupancy

    @max_occupancy.setter
    def max_occupancy(self, value):
        max_occupancy_validator(value)
        self._max_occupancy = value

    @property
    def has_balcony(self):
        return self._has_balcony

    @has_balcony.setter
    def has_balcony(self, value):
        self._has_balcony = value

    @property
    def view_type(self):
        return self._view_type

    @view_type.setter
    def view_type(self, value):
        self._view_type = value

