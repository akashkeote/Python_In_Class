# 10 if 1<2 or 20>10:
#     print("Condition is true")

if 1<2:
    x=20
    y=10
else:
    x=10
    y=20
if 1<2:
    x=20
    y=30
elif 2<3:
    x=30
    y=40
else:
    x=40
    y=50
print(x,y)

#pass block means empty block hota hai
if 1>2:
    pass
else:
    x=200
    y=300


if 1<2:
    if 2<3:
        print('a')
    else:
        print('b')

if 1<2:
    if 2<3:
        print('a')
else:
        print('b')

i=0
while i<10:
    print(i)
    i+=1
else:
    print("Loop is over")
    #unique in python, else block will run when while loop is over.

for i in 'hello world':
    print(i)

for i in [1,2,3,4]:
    print(i*i)

for i in range(10):
    i+=1
    print(i*i)

r = range(10)
print(type(r))

for i in range(100000):
    print(i*i)
    if(i==10):break

print("loop no 9 \n")
for i in range(100000):
    if i%3 == 0:
        continue
    print(i*i)
    if(i==10):break

print("loop no 10 \n")
x=[1,2,3,4,5]
for i in [1,2,3,4,5]:
    print(i*i)
    i+=1
else:
    print("Loop is over")

def foo(x,y,z):
    s=x+y+z
    return s

print(type(foo)) #<CLASS 'function'>

add=foo
print(add(2,3,4))
print(foo(2,3,4))
print(x)
print(y)
del x,y

del foo
print(add(2,3,4)) #because we deleted the function foo, but add is still pointing to the same function object.

print(id(add))
print(add('abc','def','123')) #abc def 123
# print(add('abc','def',123)) #error because we cannot add string and integer together.
def add(x,y):
    if isinstance(x,int) and isinstance(y,int):
        return x+y
    else:
        return "Invalid type"
print(add(2,3))
print(add('abc','def'))
print(add('abc',123))

def add(x,y):
    assert isinstance(x,int)
    assert isinstance(y,int)
    return x+y


print(add(2,3))
# print(add('abc','def')) #error because we cannot add string and integer together.
# print(add('abc',123)) #error because we cannot add string and integer together.
print(add(y=90,x=100))
def add(x,y,z=100):
    assert isinstance(x,int)
    assert isinstance(y,int)
    assert isinstance(z,int)
    return x+y+z    
print(add(2,3))
print(add(2,3,4))

#recreated fun body
def add(x):
    return x+2
# print(add(2,1)) override ho gaya, because function name same hai, so last defined function will be used.
print(add(2))

x=7
x=8
def add(*t):
    print(type(t))


def add(*t):
    print(type(t))
    s=0
    for i in t:
        s+=i
    return s
print(add(1,2,3,4,5))
print(add())
 
x=[1,2,3,4,5]
a,*y=x #yaha * ka matlab hai ki baki ke elements ko y mein store kar do.
print(a)
print(y)
a,*y="akash"
print(a)
print(y)

def foo(a,*y):
    print(a)
    print(y) #remaining elements will be stored in y as a tuple.
    #why this in tuple???
    #because *y is a variable length argument, so it will be stored in a tuple.
    # but list bhi ho sakta hai, but by default it is tuple.

foo(1,2,3,4,5)

def foo(*t,**k): #*t and *k not possible use **k because **k is used for keyword arguments, so it will be stored in a dictionary.
    print(type(t))
    print(t)
    print(k)

def foo(*t,a=10):
    print(t)
    print(a)

def foo(**d):
    print(d)
    print(type(d)) #<class 'dict'>

foo(a=10,b=20)
foo(c=20,d=30)

print(globals()) #yeh function ke andar ke variables ko print karega, but yeh function ke bahar ke variables ko print nahi karega.

def add(x,y):
    print(globals()) #yeh function ke andar ke variables ko print karega, but yeh function ke bahar ke variables ko print nahi karega.
    s=x+y
    g=globals() #yeh function ke andar ke variables ko print karega, but yeh function ke bahar ke variables ko print nahi karega.
    g['a']=100
    print(locals())
    return s


#global vs local
x=10
def foo():
    x=20
    return x

print(x)
print(foo()) #20
new_var=1000
def foo():
    new_var=100
    return new_var

print(foo()) #100
print(new_var) #1000

#globalkeyword
print("global keyword")
new_var=1000
def foo():
    global new_var
    print(new_var) #1000
    new_var=100
    return new_var
print(foo()) #100
