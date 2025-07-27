from model.entity.guest import Guest
from model.repository.guest_repository import GuestRepository

#test passed
guest_1 = Guest(4 , "Mahdi" , "Alipour" , 20 , "09128883430" ," 01/01/2005")
#print(guest_1)
#print(guest_1.to_tuple())
guest_repo=GuestRepository()
#test passed
#guest_repo.save(guest_1)
#test passed
#guest_repo.edited(guest_1)
#test passed
#guest_repo.delete(1)
#test passed
#print(guest_repo.find_all())
#test passed
#print(guest_repo.find_by_code(2))
#test passed
#print(guest_repo.find_by_name_family("kia" , "abbasi"))
#test passed
#print(guest_repo.find_by_phone_number("09128883430"))

