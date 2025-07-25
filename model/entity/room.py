class Room:
    def __init__(self, room_code, room_type, price_per_night, floor,
                 is_booked, max_occupancy , has_balcony, view_type):
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



    #todo:getter/setter -->validation