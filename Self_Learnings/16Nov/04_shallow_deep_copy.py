# Shallow aur Deep Copy - Hinglish Notes

import copy

# Direct assignment copy nahi banata; dono variables same object ko refer karte hain.
original = [1, 2, 3]
reference = original
original.append(4)
print(reference)  # [1, 2, 3, 4]

# Shallow copy outer list ki nayi copy banata hai.
x5 = [1, 2, 3, 4, [5, 6, 7]]
x6 = x5.copy()
print(x5 is x6)  # False: outer lists alag hain
print(x5[4] is x6[4])  # True: nested list shared hai

x6[4].append(8)
print(x5)  # Nested change original mein bhi dikhega
print(x6)

# Deep copy nested objects ki bhi separate copies banata hai.
x7 = [1, 2, 3, 4, [5, 6, 7]]
x8 = copy.deepcopy(x7)
print(x7 is x8)  # False
print(x7[4] is x8[4])  # False: nested lists bhi alag hain

x8[4].append(8)
print(x7)  # Original unchanged rahega
print(x8)

# == values compare karta hai; is object identity compare karta hai.
print(x7 == x8)
print(x7 is x8)
