# class A:
#     def foo(self):
#         return "Hello A"
# class B(A): 
#     def foo2(self):
#         return "Hello B"
# class C(B):
#     def foo3(self):
#         return "Hello C"
# c=C()
# print(c.foo())
# #MRO
# print(C.__mro__) # ye class ka docstring print karega.
# #(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
# print("NOOOOOOOOO")
# print(c.__init__()) # ye None print karega, kyuki ye object ka init call ho raha hai, class ka nahi.

# #overriding
# class D(C):
#     def foo(self):
#         return "Hello D"

# d=D()
# print(d.foo()) 


# #defining constructor challenging
# class Emp:
#     def __init__(self,name,salary,age):
#         self.name=name
#         self.salary=salary
#         self.age=age

# class Manager(Emp):
#     def __init__(self,project,name,salary,age):
#         self.project=project
#         super(self).__init__(name,salary,age)#explicitly parent constructor ko call kiya hamne
#         # and ye bad design bhi mana jayega 
#         # because we are not using the parent's constructor properly
# #python me override bhi hota hai init to constructor nahi bol sakte init kko ham 
# class SuperManager(Emp):
#     def __init__(self,foo,name,salary,age):
#         self.foo=foo
#         super(self).__init__(name,salary,age)#explicitly parent constructor ko call kiya hamne
# m=Manager("Project1","akash",1000,25)
# print(m.project)
# print(m.name) # ye error dega, kyuki hamne parent ka init call nahi kiya, to name attribute create nahi hua.



from importlib import abc
import math


class A:
    def foo(self):
        return 10

class B(A):
    def foo1(self):
        return 20

class C(A):
    def foo2(self):
        return 30
class C(A):
    def foo1(self):
        return 40
    def foo2(self):
        return 50
class D(C,B): #yaha ham A nahi likh sakte 
    #MRO nahi banega nahito
    pass

d=D()
print(d.foo()) # ye 10 print karega, kyuki ye A ka method hai
print(d.foo1()) # ye 20 print karega, kyuki ye B ka method hai
print(d.foo2()) # ye 50 print karega, kyuki ye C ka method

class Emp:
    @staticmethod
    def whoami():
        return "I am an employee"

class Manager(Emp):
    pass

m=Manager()
print(m.whoami()) # ye I am an employee print karega, kyuki Manager class me whoami method nahi hai, to parent class ka method call hoga.
print(Manager.whoami()) # ye bhi I am an employee print karega, kyuki Manager class me whoami method nahi hai, to parent class ka method call hoga.


class Emp:
    @classmethod
    def whoami(cls):
        # return "I am an employee class method"
        return str(cls)

print(Emp.whoami()) # ye <class '__main__.Emp'> print karega, kyuki Emp class ka method call ho raha hai.
class Manager(Emp):
    pass

print(Manager.whoami()) # ye <class '__main__.Manager'> print karega, kyuki Manager class ka method call ho raha hai.

class Emp:
    cnt=0
    @classmethod
    def inc_count(cls):
        cls.cnt+=1
        return cls.cnt
    @classmethod
    def whoami(cls):
        return str(cls)

class Cartesian:
    
    def __init__(self,x,y):
        self.x=x
        self.y=y
    @classmethod
    def from_polar(cls,r,theta):
        x=r*math.cos(theta)
        y=r*math.sin(theta)
        return cls(x,y)
c=Cartesian.from_polar(10,20)
print(c.x)
print(c.y)
print(type(c))

class Complex(Cartesian):
    pass
e=Complex.from_polar(100,200)
print(type(e))

#sttatic method ko based class ka inherit nahi kar sakte derived me then 
# class method ka concept aata hai waha par


   
    
from abc import ABC, abstractmethod 
#for abstract class
class Emp(ABC):
    @abstractmethod
    def show(self):
        pass

# obj1=Emp() #abstract class ka
#direct object nahi banta hai
# print(obj1.show())

class PaymentGatway(ABC):
    @abstractmethod
    def pay(self):
        pass
class RazerPay(PaymentGatway):
    def pay(self):
        print("RazerPay paying ...")
class Purchase:
    def __init__(self,gateway):
        self.gateway=gateway
    def checkout(self):
        print("Checkout....")
        self.gateway.pay()

gateway1=RazerPay()
purchase=Purchase(gateway1)

purchase.checkout()

class PayTm:
    def pay(self):
        print("Paytm karo ....")
class RazerPay:
    def pay(self):
        print("RazerPay paying ...")

class Purchase:
    def __init__(self,gateway):
        self.gateway=gateway
    def checkout(self):
        print("Checkout....")
        self.gateway.pay()
gateway2=PayTm()
gateway1=RazerPay()
purchase=Purchase(gateway2)
purchase.checkout()








