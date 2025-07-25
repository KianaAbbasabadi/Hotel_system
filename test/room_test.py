from model.entity.room import Room

room_1 = Room(1, "big", 1200, 3, False, 2, True, "City")
print(room_1)


room_tuple = room_1.to_tuple()
print(room_tuple)
