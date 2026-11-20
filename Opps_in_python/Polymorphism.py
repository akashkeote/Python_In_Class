class Car:
    def fuelType(self): #self dena zaruri hai context value 
        return "Petrol or Diesel"

class ElectricCar(Car):
    def fuelType(self):
        return "Electric Charging"

a=ElectricCar()
print(a.fuelType())
c=Car()
print(c.fuelType())