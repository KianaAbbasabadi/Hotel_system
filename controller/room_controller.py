from model.entity.room import Room
from model.repository.room_repository import RoomRepository

class RoomController:
    def save(self, room_code, room_type, price_per_night, floor, is_booked, max_occupancy, has_balcony, view_type):
        try:
            room = Room(room_code, room_type, price_per_night, floor, is_booked, max_occupancy, has_balcony, view_type)
            room_repository = RoomRepository()
            room_repository.save(room)
            return True, f"Room saved {room}"
        except Exception as e:
            return False, f"Error saving room {e}"

    def edit(self, room_code, room_type, price_per_night, floor, is_booked, max_occupancy, has_balcony, view_type):
        try:
            room = Room(room_code, room_type, price_per_night, floor, is_booked, max_occupancy, has_balcony, view_type)
            room_repository = RoomRepository()
            room_repository.edit(room)
            return True, f"Room edited {room}"
        except Exception as e:
            return False, f"Error editing room {e}"

    def delete(self, room_code):
        try:
            room_repository = RoomRepository()
            room_repository.delete(room_code)
            return True, f"Room deleted {room_code}"
        except Exception as e:
            return False, f"Error deleting room {e}"

    def find_all(self):
        try:
            room_repository = RoomRepository()
            rooms = room_repository.find_all()
            return True, rooms
        except Exception as e:
            return False, f"Error finding rooms {e}"

    def find_by_code(self, room_code):
        try:
            room_repository = RoomRepository()
            room = room_repository.find_by_code(room_code)
            return True, room
        except Exception as e:
            return False, f"Error finding room by code {e}"

    def find_by_room_type(self, room_type):
        try:
            room_repository = RoomRepository()
            rooms = room_repository.find_by_room_type(room_type)
            return True, rooms
        except Exception as e:
            return False, f"Error finding rooms by type {e}"

    def find_by_price_per_night(self, price_per_night):
        try:
            room_repository = RoomRepository()
            rooms = room_repository.find_by_price_per_night(price_per_night)
            return True, rooms
        except Exception as e:
            return False, f"Error finding rooms by price {e}"

    def find_by_floor(self, floor):
        try:
            room_repository = RoomRepository()
            rooms = room_repository.find_by_floor(floor)
            return True, rooms
        except Exception as e:
            return False, f"Error finding rooms by floor {e}"

    def find_by_is_booked(self, is_booked):
        try:
            room_repository = RoomRepository()
            rooms = room_repository.find_by_is_booked(is_booked)
            return True, rooms
        except Exception as e:
            return False, f"Error finding rooms by booking status {e}"

    def find_by_max_occupancy(self, max_occupancy):
        try:
            room_repository = RoomRepository()
            rooms = room_repository.find_by_max_occupancy(max_occupancy)
            return True, rooms
        except Exception as e:
            return False, f"Error finding rooms by max capacity {e}"

    def find_by_has_balcony(self, has_balcony):
        try:
            room_repository = RoomRepository()
            rooms = room_repository.find_by_has_balcony(has_balcony)
            return True, rooms
        except Exception as e:
            return False, f"Error finding rooms by balcony availability {e}"

    def find_by_view_type(self, view_type):
        try:
            room_repository = RoomRepository()
            rooms = room_repository.find_by_view_type(view_type)
            return True, rooms
        except Exception as e:
            return False, f"Error finding rooms by view {e}"




