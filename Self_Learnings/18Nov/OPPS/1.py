class Emp:
    pass

e=Emp()
e2 = Emp()
print(e==e2,"false")

print(isinstance(e,Emp))
print(type(e))
print(dir(Emp))
# Python prototyping approach follow karta hai.
# Class ka object banne ke baad bhi usme naye attributes add kar sakte hain.
e.salary = 10000
e.name="John"
print(e.name)
e2.name="Doe"
print(e2.name)

del e,e2

class Emp:
    'class to represent an employee'
    # self instance ke liye hota hai; class-level values class ke naam se access hoti hain.
    empId=1000
    count=0
    @staticmethod
    def whoami():
        return 'Emp Object'
    def __init__(self,name='unknown',salary=0,age=0,grade=1): # ye initializer hai; default values overloading jaisa kaam karti hain.
        self.name=name
        self.salary=salary
        self.age=age
        self.grade=grade
        # Single underscore private convention hai, Python me strict private nahi hota.
        self._foo=100
        Emp.count+=1
        self.id=Emp.empId
        Emp.empId+=1 #auto generate emp id

    def __repr__(self): #shell repr
        return '<{},{},{},{}>'.format(self.name,self.salary,self.age,self.grade)
    def __str__(self): #toString()
        return '{},{},{},{}'.format(self.name,self.salary,self.age,self.grade)
    def __add__(self,v):  #obj + v1+v2
        #if isinstance(v,Emp): #do something
        isinstance(v,Emp)
        if(type(self.salary)==type(v)):
            self.salary+=v
            return self

        self.salary+=v
        return self
    def __radd__(self,v): # v + obj ke liye reverse addition.
        self.salary+=v
        return self

        return self + v
    def __mod__(self,v): # obj % v se bonus percentage calculate hota hai.
        self.bonus=self.salary*(v/100)
        return self.bonus
    def __lt__(self,e): # obj < e salary comparison karta hai.
        if isinstance(e,Emp):
            return self.salary < e.salary
    
    def compute_bonus(self): #methods
        if self.grade>=4:self.bonus = self.salary*20/100
        else: self.bonus = self.salary*10/100

    def __del__(self): # object delete hone par destructor call ho sakta hai.
        if Emp.count > 0:
            Emp.count-=1
        print('Destructor called')

e=Emp('abc')
print(e.name)
print(e.age)
# print(e.bonus) # Abhi compute_bonus() call nahi hua, isliye bonus available nahi hai.
e.compute_bonus()
print(e.bonus) # compute_bonus() call hone ke baad bonus available ho gaya.
print(e._foo) # Single underscore private convention hai, guaranteed private nahi.
print(dir(e)) # dir() private-convention wale attributes ko bhi dikhata hai.
e._foo=200 # Bahar se bhi is attribute ko change karna possible hai.
print(e._foo) 

print(e)
print(e.name)
# Existing object ki values reset karne ke liye __init__ manually call kar sakte hain.
e.__init__('def',1000,2,6)
print(e)
print(e.name)
print(e.salary)

print(e.__doc__) # ye class ka docstring print karega.
print(Emp.whoami()) # static method ko object ke bina call kar sakte hain.

e=Emp()

e=Emp('abc',1000)
print(e)
print(e+100)
e.compute_bonus()
print(e.bonus)
print(e%50) # salary ka 50 percent bonus calculate hota hai.
print(e.bonus)
e=Emp()
print(e+5)
print(e+5+  10)
print(10+e)
e1=Emp()
print(e<e1)
print(str(e))
print()

















    
