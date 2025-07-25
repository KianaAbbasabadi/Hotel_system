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



   # todo:getter/setter--> validation





