class Car:
    totalcnt=0
    def fuelType(self): #self dena zaruri hai context value 
        return "Petrol or Diesel"
    def __init__(self,brand,model):
        Car.totalcnt+=1
        self.brand=brand
        self.__model=model
    @staticmethod
    def general_desp(): # static method ko self ya cls nahi chahiye
        return "Cars are means for transport"
    @property
    def get_model(self):
        return self.__model

class ElectricCar(Car):
    def fuelType(self):
        return super().fuelType()

#class ke pass available hai par instance/fun ke pass nahi
#obj ke pass nahi 
ec=ElectricCar("Toyota","akash wala model")
print(ec.general_desp())
e=Car("model","jay wala")
print(ElectricCar.general_desp())
# print(e.__model) cant able to use this private
print(e.get_model)


print(isinstance(e,ElectricCar))
print(isinstance(ec,Car))