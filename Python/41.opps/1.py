class computer:
    pass
com1=computer()

class Car:
    brand=None
    model=None

my_car=Car()
print(my_car) #<__main__.Car object at 0x0000011A4C774590>
#object banate time hi value add karna hai to
class dummy:
    def __init__(mybrand,mymodel):
        brand=mybrand
        model=mymodel
# my_dummy=dummy("AKash",2004)
# print(my_caar.brand)
#self chahiye link establish karne ke liye

class Caar:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

my_caar=Caar("AKash",2004)
print(my_caar.brand)
my_new_car=Caar("Jaya",2003)
print(my_new_car.brand)
my_caar.brand = "Jay"
print(my_caar.brand)


class ar:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def full_name(self):
        return f"{self.brand} {self.model}"


my_ar=ar("AKash",2004)
print(my_ar.full_name())  #AKash 2004

#inheritance



