# Encapsulation
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand


c = Car("akash", "s3 pro")
print(c.get_brand())
