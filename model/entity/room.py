class Room:
    def __init__(self, room_code , room_type , price_per_night , floor ):
        self.room_code = room_code
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.floor = floor


    def __repr__(self):
        return f"{self.__dict__}"


    #todo:getter/setter -->validation