import sys
x=5
print(isinstance(x,int))
z=6.7
print(type(z))
x=7
x=x+1
print(x)
++x
print(x)
y=6
res = x++ + ++x
print(res)
p = 0 if x>y else 1
print(p)
+x
print(x)

print(-x)
print(x<<2)
print(y)

print(2<3 & 3<4)
print(2<3 and 3<4)

print(2<3 | 3<4)
print(2<3 or 3<4)

print(1.5 ** 1199)

# print(z<<3)

print(2**0.5)
z=6.7
print(z==6.7)
# -1**0.5
print(-1**0.5)
print("difference is there")
print((-1)**0.5)

print(2**3**4)
print(2**81)

cl = 1;
c2 = 2;
c3 = complex(cl,c2)
print(c3)
print(type(c3))
c=1+2j
print(c3+c)

# print(c3//c)
print(c3/c)
print(c**c3)

#comparison of complex numbers not work
# print(c3>c)
print(c3==c);

s1 = 'a'
print(type(s1))
print(sys.getsizeof(s1))


#operation on strings
c1="hello"
c2="hello"
print(c1+c2)
print(c1==c2)
s3="sample string"
s4="""this is
para 
graph"""
print(s4)

filepath=r"C:\Users\akash.keote\Desktop\python\sample.txt"
print(filepath)

s="akash keote"
print(s[6]);

print(isinstance(x,float))
s = "the price of %s is %f for %d items"
s=s%('apple', 5.5, 2);
print(s)

s1 = "the price of %s is %4.2f for %-100d of them"
print(s1%('apple', 5.5, 2))

s6 = "the price of {} is {} for {} items"
print(s6.format('apple',5.5,4))



# Slice vs. stride
#s2
# Slicing selects a portion of a sequence:
# sequence[start:stop]
# The start index is included, but the stop index is excluded.
#
# Stride, also called step, controls how many positions to move between
# selected elements:
# sequence[start:stop:step]
#
# Examples:
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])    # [1, 2, 3] - slice with the default stride of 1
print(numbers[::2])    # [0, 2, 4] - every second element
print(numbers[1::2])   # [1, 3, 5] - every second element, starting at index 1
print(numbers[::-1])   # [5, 4, 3, 2, 1, 0] - reverse the sequence

s2='hello world'
print(s2)
print(s2.center(50,"X"));

#pehle X then 50 is error bro
print(s2.split())
print(s2.find('o'));
print(s2.index('o'));
print(s2[s2.find('h')])



print(str(dir(s2)))

