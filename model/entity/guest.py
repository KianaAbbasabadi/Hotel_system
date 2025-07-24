class Guest:
    def __init__(self,guest_code ,name,family,age, phone_number ):
        self.guest_code = guest_code
        self.name = name
        self.family = family
        self.age = age
        self.phone_number = phone_number



    def __str__(self):
        return f"{self.__dict__}"



   # todo:getter/setter--> validation





