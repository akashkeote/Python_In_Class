# 13 Nov - Python Fundamentals

import sys

# Type check karna.
x = 5
print(isinstance(x, int))
z = 6.7
print(type(z))

# Python mein ++x aur x++ increment operators nahi hain.
x = 7
x += 1
print(x)
x += 1
print(x)

# Multiple values ko expression mein clearly calculate karein.
y = 6
result = x + 1 + x + 1
print(result)

# Unary plus/minus aur bitwise left shift.
print(+x)
print(-x)
print(x << 2)
print(y)

# and/or ko comparison ke saath parentheses mein likhna clear hota hai.
print((2 < 3) & (3 < 4))
print(2 < 3 and 3 < 4)
print((2 < 3) | (3 < 4))
print(2 < 3 or 3 < 4)

# Exponentiation right-to-left associate hoti hai: 2 ** (3 ** 4).
print(2 ** 3 ** 4)
print(2 ** 81)
print(2 ** 0.5)

# Floating-point exponent bahut bada ho sakta hai, isliye practical range rakhein.
print(1.5 ** 10)

# Comparisons aur complex numbers.
print(z == 6.7)
print(-1 ** 0.5)  # Python precedence ke wajah se -(1 ** 0.5)
print((-1) ** 0.5)  # Complex result

# Complex number banana.
real_part = 1
imaginary_part = 2
complex_number = complex(real_part, imaginary_part)
print(complex_number)
print(type(complex_number))

other_complex = 1 + 2j
print(complex_number + other_complex)
print(complex_number / other_complex)
print(other_complex ** complex_number)
print(complex_number == other_complex)
# Complex numbers par < ya > comparison supported nahi hota.

# String basics.
s1 = "a"
print(type(s1))
print(sys.getsizeof(s1))

c1 = "hello"
c2 = "hello"
print(c1 + c2)
print(c1 == c2)

# Multiline string.
s3 = "sample string"
s4 = """this is
para
graph"""
print(s3)
print(s4)

# Raw string backslashes ko escape nahi karta.
file_path = r"C:\Users\akash.keote\Desktop\python\sample.txt"
print(file_path)

s = "akash keote"
print(s[6])
print(isinstance(x, float))

# Old-style formatting.
price_text = "the price of %s is %f for %d items"
print(price_text % ("apple", 5.5, 2))

# Recommended modern formatting.
print(f"the price of apple is {5.5:.2f} for {2} items")

# Slicing: stop index include nahi hota.
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])
print(numbers[::2])
print(numbers[1::2])
print(numbers[::-1])

s2 = "hello world"
print(s2)
print(s2.center(50, "X"))
print(s2.split())
print(s2.find("o"))
print(s2.index("o"))
print(s2[s2.find("h")])
