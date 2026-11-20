#inheritance
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def show(self):
        return "this is method of Car class"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model) #super claass 
        self.battery_size=battery_size
e=ElectricCar("Ola","s2 pro","4kWH")
print(f"{e.battery_size},{e.brand},{e.model}")
print(f"{e.show()}")
print(e.show())



