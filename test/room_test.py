from model.entity.room import Room
from model.repository.room_repository import RoomRepository
from controller.room_controller import RoomController

room_1 = Room(1, "big", 1200, 1, False, 4, True, "City")
room_2 = Room(2, "small", 1400, 3, True, 2, True, "sea")
#print(room_1)

#test passed
#room_tuple = room_1.to_tuple()
#print(room_tuple)

#room_repo = RoomRepository()
#test passed
#room_repo.save(room_1)
#room_repo.save(room_2)
#test passed
#room_repo.edite(room_1)
#test passed
#room_repo.delete(room_1)
#test passed
#print(room_repo.find_all())
#test passed
#print(room_repo.find_by_room_type("big"))
#test passed
#print(room_repo.find_by_code(1))
#test passed
#print(room_repo.find_by_floor(3))
#test passed
#print(room_repo.find_by_is_booked(True))
#test passed
#print(room_repo.find_by_max_occupancy(2))
#test passed
#print(room_repo.find_by_has_balcony(True))
#test passed
#print(room_repo.find_by_price_per_night(1200))
#test passed
#print(room_repo.find_by_view_type("sea"))


room_controller = RoomController()
#test passed
#print(room_controller.save(3 , "big" , 1300 ,2 , True , 4 , False , "street"))
#test passed
#print(room_controller.edit(3 , "big" , 1600 ,2 , True , 4 , False , "street"))
#test passed
#print(room_controller.delete(2))
#test passed
#print(room_controller.find_all())
#test passed
#print(room_controller.find_by_room_type("big"))
#test passed
#print(room_controller.find_by_code(3))
#test passed
#print(room_controller.find_by_price_per_night(1600))
#test passed
#print(room_controller.find_by_floor(1))
#test passed
#print(room_controller.find_by_is_booked(True))
#test passed
#print(room_controller.find_by_max_occupancy(4))
#test passed
#print(room_controller.find_by_has_balcony(True))




