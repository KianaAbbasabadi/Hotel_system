from model.entity.guest import Guest
from model.repository.guest_repository import GuestRepository

class GuestController:
    def save(self, guest_code ,name,family,age, phone_number, birth_date ):
     try:
        guest=Guest(guest_code ,name,family,age, phone_number, birth_date )
        guest_repository=GuestRepository()
        guest_repository.save(guest)
        return True , f"guest saved{guest}"
     except Exception as e:
         return False, f"Error saving guest {e}"


    def edite(self,guest_code ,name,family,age, phone_number, birth_date ):
        try:
            guest = Guest(guest_code, name, family, age, phone_number, birth_date)
            guest_repository = GuestRepository()
            guest_repository.edite(guest)
            return True, f"guest edited{guest}"
        except Exception as e:
            return False, f"Error editing guest {e}"

    def delete(self, guest_code):
        try:
            guest_repository = GuestRepository()
            guest_repository.delete(guest_code)
            return True, f"guest deleted{guest_code}"
        except Exception as e:
            return False, f"Error deleting guest {e}"


    def find_all(self):
         try:
             guest_repository = GuestRepository()
             return True, guest_repository.find_all()
         except Exception as e:
             return False, f"Error finding guest {e}"
    def find_by_code(self, guest_code):
        try:
            guest_repository = GuestRepository()
            return True, guest_repository.find_by_code(guest_code)
        except Exception as e:
            return False, f"Error finding guest {e}"
    def find_by_name_family(self, name , family):
       try:
            guest_repository = GuestRepository()
            return True, guest_repository.find_by_name_family(name, family)
       except Exception as e:
            return False, f"Error finding guest {e}"
    def find_by_phone_number(self, phone_number):
       try:
           guest_repository = GuestRepository()
           return True, guest_repository.find_by_phone_number(phone_number)
       except Exception as e:
           return False, f"Error finding guest phone number {e}"