class Car:
    totalcnt=0
    def fuelType(self): #self dena zaruri hai context value 
        return "Petrol or Diesel"
    def __init__(self):
        Car.totalcnt+=1
        # self.brand=brand

class ElectricCar(Car):
    def fuelType(self):
        return super().fuelType()

c=Car()
e=ElectricCar()
print(e.fuelType())
print(Car.totalcnt) #2
#without it 
print(c.totalcnt) #2
d=Car()
print(d.totalcnt) #3 3 nahi hona hame par


