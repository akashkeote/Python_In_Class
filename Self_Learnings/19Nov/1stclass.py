#constructor bas init se banao and start karo and then use karo 
#python me default parametrized kuch nahi default init banao and karo
#indirect way of invoking an functionm 
class Emp:
    def __foo__(self):
        return "Hello akash"
    def copy(self):
        return copy.deepcopy(self)
    def __myfun__(self):
        return 10
    def salary(self):
        return 100
    

class Person(Emp):
    def salary(self):
        return 10

p = Emp()
print(p.salary())
p=Person()
print(p.salary())


# e=Emp.__foo__() #indirect way of invoking an function

#python are not strongly typed language, so we can add any type of data to the class object

