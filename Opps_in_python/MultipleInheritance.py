class Battery:
    def info(self):
        return "this is info battery"
class Engine:
    def info(self):
        return "this is info Engine"
class ElectricCar(Engine,Battery):
    def show(self):
        return "thois is show"
my_new = ElectricCar()
print(my_new.info())

