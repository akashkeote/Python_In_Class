# # a=True;
# # b=False;
# # print(type(a))
# # print(type(b))

# # print(a and b)
# # print(a or b)

# # print(not a)

# # print(a+1)
# # print(b+1)
# # print(a<<10)

# # a=None
# # print(a)
# # print(b+1)


# # s1= "hello world"
# # print(s1.startswith('j'))
# # print(s1.endswith("ay"))

# # s2 = s1*5
# # print(s2)


# # print(s2.split(sep='o'))
# # print(s2.split())

# #join function
# # print("$".join(s2.split()))
# # print("akash".join(s2.split()))


# # print(s1.replace('l','a'))
# # # rint(help())
# # x1 = [1,2.5,1+2j,'abc']
# # print(x1)
# # print(type(x1))
# # print(x1[4:7])
# # print(dir(x1))
# # print(x1[0])
# # x1[0]=100
# # print(x1)
# # print(x1.append(1000))
# # print(x1)
# # print(x1.pop())
# # print(x1.pop(0))
# # print(x1.reverse())
# # print(x1[::-1])
# # x4 = x1.reverse()
# # print(x1)
# # print(x4)
# # print(x1.reverse())
# # #numbers we can able to sort but the mixing values we cant able to sort 
# # x3=[745,4,6,3,2,1,0]
# # print(x3.sort())
# # x1.append(x3)
# # print(x1)
# # #index of function
# # print(x1.index(2.5))
# # print(len(x1))
# # print(len(x3))
# # x7=x3
# # x3.append(8)
# # print(x7)
# #yaha reference ko point karta na ki copy ko #[0, 1, 2, 3, 4, 6, 745, 8]

# # #but we want the shallow copy of the list then we can use the copy function
# # x8=x3.copy() # later they introduced the copy module to do the shallow and deep copy of the list
# # #before python 3 we did not have the copy function in the list so we can use the copy module to do the shallow and deep copy of the list
# # x3.append(9)
# # print(x8) #[0, 1, 2, 3, 4, 6, 745, 8]

# # print(id(x3)==id(x7))
# # print(id(x8)==id(x3))
# # #== element wise comparison it does not check the reference of the object
# # print(x7 is x3)
# # print(x8 is x3)

# # x11 = [5,6,7,8]
# # print(x8 in x11)
# # print('11' in s1)

# # #deep vs shallow copy
# # x5 = [1,2,3,4,[5,6,7]]
# # x6 = x5.copy()
# # print(x5 is x6)  # False: a new outer list
# # print(x5[4] is x6[4])  # True: the nested list is shared

# # x6[4].append(8)
# # print(x5)  # The nested change is visible in both lists
# # print(x6)

# # # deep copy example
# # import copy

# # x7 = [1,2,3,4,[5,6,7]]
# # x8 = copy.deepcopy(x7)
# # print(x7 is x8)  # False
# # print(x7[4] is x8[4])  # False: the nested list is also copied

# # x8[4].append(8)
# # print(x7)  # The original is unchanged
# # print(x8)



# #tuple
# t1 = (1,2,3,4)
# print(t1)
# print(type(t1))
# # t1[0] = 100  # This will raise an error because tuples are immutable
# print(t1[0])
# print(t1[1:3])

# x,y,z,t = t1
# print(x,y,z,t)


# def foo(a,b):
#     return a+b, a-b,a*b,a//b

# print(foo(10,5))
# a,s,m,d = foo(10,5)
# print(a)#15
# print(s)#5
# print(m)#50
# print(d)#2


#dictionary 
emp={
    'name':'akash',
    'age':25,
    'city':'Mumbai',
    'projects':['project1','project2','project3'],

}
print(type(emp))
# print(emp*3)
#print(emp[0]) #error
print(emp['projects'])
print('projects1' in emp) #false
print('projects' in emp) #true

print(emp.keys()) #list of keys
print(emp.values()) #list of values

print(emp.items())#list of tuples both key and value

#print(emp['name']='jay')#error

emp['name'] = 'jay'
print(emp)
view=emp.values()
print(type(view)) #<class 'dict_values'>
#print(view[0])      #error because view is not a list but a view object which is iterable but not subscriptable


emp.popitem() #removes the last item from the dictionary
print(emp) #projects key is removed from the dictionary

d1={1:2,2:3,3:4}
d2={4:5,5:6,6:7}
#d1+d2#error
d1.update(d2) #merges d2 into d1
print(d1) # {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7}

d2 ={1:3,1:6,1:9} #duplicate keys are not allowed in dictionary so the last value will be taken
print(d2) # {1: 9} 
#cannot use list as a dict key 
#unhashable types: 'list' because list is mutable and can be changed so it cannot be used as a key in dictionary
#example
# d3 = {[1,2,3]: '34'} #error
# print(d3)

stringdict = {'name':'akash','age':25,'city':'Mumbai','projects':['project1','project2','project3']}
   
print(stringdict['projects'][0]) #project1
print(stringdict['city'])#Mumbai
print('projects' in stringdict) #True
#set
s1 = {1,2,3,4,5}
print(type(s1))
s2={4,5,6,7,8}
print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8}
print(s1.intersection(s2)) # {4, 5}
print(s1|s2) # {1, 2, 3, 4, 5, 6, 7, 8}
print(s1&s2) # {4, 5}

print(s1-s2) # {1, 2, 3} unique of s1
tp = (1,2,3,4,5)
sp=set(tp)
print(sp) # {1, 2, 3, 4, 5}
print(id(sp))
frozenset1 = frozenset(tp)
print(frozenset1) # frozenset({1, 2, 3, 4, 5})
#tuple version of your set which is immutable and hashable so it can be used as a key in dictionary










