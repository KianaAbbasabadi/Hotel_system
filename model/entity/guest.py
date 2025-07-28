
from model.tool.validation import *


class Guest:
    def __init__(self,guest_code ,name,family,age, phone_number, birth_date ):
        self.guest_code = guest_code
        self.name = name
        self.family = family
        self.age = age
        self.phone_number = phone_number
        self.birth_date = birth_date



    def __str__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return (self.guest_code, self.name, self.family, self.age, self.phone_number , self.birth_date)









    @property
    def guest_code(self):
        return self._guest_code
    
    @guest_code.setter
    def guest_code(self, value):
        guest_code_validator(value)
        self._guest_code = value


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        name_validator(value)
        self._name = value


    @property
    def family(self):
        return self._family

    @family.setter
    def family(self, value):
        family_validator(value)
        self._family = value


    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        age_validator(value)
        self._age = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        phone_number_validator(value)
        self._phone_number = value


    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        birth_date_validator(value)
        self._birth_date = value




