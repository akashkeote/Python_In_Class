class Emp:
    pass

e=Emp()
e2 = Emp()
print(e==e2)

print(isinstance(e,Emp))
print(type(e))
print(dir(Emp))
# python follow the prototyping appraoch 
# means we can create a class and then create an object of that class and then we can add attributes to that object.
e.salary = 10000
e.name="John"
print(e.name)
e2.name="Doe"
print(e2.name)

del e,e2

class Emp:
    'class to represent an employee'
    #hame self har bar likhna nahi padta 
    #class level ke liye hi hum likhte hai self ko
    empId=1000
    @staticmethod
    def whoami():
        return 'Emp Object'
    def __init__(this,name='unknown',salary=0,age=0,grade=1): #initliazer hai na ki constructor hai ye
        this.name=name
        this.salary=salary
        this.salary=salary
        this.age=age
        this.grade=grade
        #PRIVATE BANANE KE LIYE
        this._foo=100#private variable but not guaranteed in python private
#constructor overloading is not possible in python but we can achieve the same by using default values in the constructor.
        Emp.count+=1
        this.id=Emp.empId
        Emp.empId+=1 #auto generate emp id
        if Emp.count>1:
            raise Exception('Only one object can be created')

    def __repr__(self): #shell repr
        return '<{},{},{},{}>'.format(self.name,self.salary,self.age,self.grade)
    def __str__(self): #toString()
        return '{},{},{},{}'.format(self.name,self.salary,self.age,self.grade)
    def __add__(self,v):  #obj + v1+v2
        #if isinstance(v,Emp): #do something
        self.salary+=v
        return self
    def __radd__(self,v): #v + obj
        self.salary+=v
    def __mod__(self,v): #obj % v
        self.bonus=self.salary*(v/100)
    def __it__(self,e): #obj < e
        return 'abc'
    def compute_bonus(self): #methods
        print(self.grade)
        if self.grade>=4:self.bonus = self.salary*20/100
        else: self.bonus = self.salary*10/100

    def __del__(self): #destructor
        print('Destructor called ')
        Emp.count-=1

    def __

e=Emp('abc')
print(e.name)
print(e.age)
# print(e.bonus) # INVOKE NAHI HUA HAI ABHI 
e.compute_bonus()
print(e.bonus) # INVOKE HUA HAI ABHI 
print(e._foo) #private variable but not guaranteed in python private
print(dir(e)) # ye private variable ko bhi show karega
e._foo=200 # ye bhi possible hai but ye private variable ko change kar raha hai
print(e._foo) 

# print(e.__del__())#private variable ko delete karne ke liye ye method use karte hai
print(e)
print(e.name)
#Unknown
print(e._init__('def',1000,2,6)) # ye method ko call karne ke liye use karte hai
print(e)
print(e.name)
print(e.salary)
del e
e=Emp()
print(e.__doc__) # ye class ka docstring print karega

e=Emp('abc',1000)
print(e)
print(e+100)
e.compute_bonus()
print(e.bonus)
print(e%50)
print(e.bonus)
e=Emp()
print(e+5)
print(e+5+  10)
print(10+e)
e1=emp()
print(e<e1)
print(str(e))
print()














    
