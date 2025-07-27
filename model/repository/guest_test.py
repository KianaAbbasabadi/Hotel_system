from model.entity.guest import Guest
from model.repository.guest_repository import GuestRepository
from controller.guest_controller import GuestController

#test passed
#guest_1 = Guest(4 , "Mahdi" , "Alipour" , 20 , "09128883430" ," 01/01/2005")
#print(guest_1)
#print(guest_1.to_tuple())
#guest_repo=GuestRepository()
#test passed
#guest_repo.save(guest_1)
#test passed
#guest_repo.edite(guest_1)
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
guest_controller = GuestController()

#test passed
#print(guest_controller.delete(10))
#test passed
#print(guest_controller.edite(4 , "Mani" , "Alipour" , 20 , "09128883430" ," 01/01/2005"))
#test passed
#print(guest_controller.find_all())
#test passed
#print(guest_controller.find_by_code(2))
#test passed
#print(guest_controller.save(10, "sanam" , "rahimi" , 26 , "09126953410" ," 01/07/2009"))
#test passed
#print(guest_controller.find_by_name_family("sanam" , "rahimi"))
#test passed
#print(guest_controller.find_by_phone_number("09128883430"))