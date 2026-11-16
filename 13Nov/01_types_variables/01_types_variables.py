# 13 Nov: Types aur Variables
# Variable kisi value ko store karne ke liye naam hota hai.

import sys

x = 5
print(isinstance(x, int))  # isinstance check karta hai ki x int hai ya nahi.

z = 6.7
print(type(z))  # type object ka data type batata hai.

# Python mein int ki precision practically unlimited hoti hai.
big_number = 2 ** 81
print(big_number)

# Python mein separate char type nahi hota.
# Single character bhi string hi hota hai.
character = "a"
print(type(character))

# None ka matlab hota hai ki variable ke paas abhi koi value nahi hai.
empty_value = None
print(empty_value)
print(type(empty_value))

print(sys.getsizeof(character))  # Object ka approximate memory size.
