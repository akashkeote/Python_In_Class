class Car:
    totalcnt=0
    def fuelType(self): #self dena zaruri hai context value 
        return "Petrol or Diesel"
    def __init__(self,brand):
        Car.totalcnt+=1
        self.brand=brand
    @staticmethod
    def general_desp(): # static method ko self ya cls nahi chahiye
        return "Cars are means for transport"

class ElectricCar(Car):
    def fuelType(self):
        return super().fuelType()

#class ke pass available hai par instance/fun ke pass nahi
#obj ke pass nahi 
e=Car("Toyota")
print(e.general_desp())
print(Car.general_desp())


