# 13 Nov: Operators aur Numbers

# Arithmetic operators: +, -, *, /, //, %, **
x = 7
x += 1  # Python mein x++ nahi hota; += 1 use karte hain.
print(x)

# Unary plus aur minus.
print(+x)
print(-x)

# Floor division // quotient ka floor result deta hai.
print(7 // 2)
print(7 % 2)  # Remainder.

# Exponentiation right-to-left associate hoti hai.
print(2 ** 3 ** 4)  # Same as 2 ** (3 ** 4)
print(2 ** 0.5)  # Square root of 2.

# Bitwise left shift number ko bits ke level par shift karta hai.
print(x << 2)

# Comparisons chain ki ja sakti hain.
print(1 < 2 < 3)
print((2 < 3) and (3 < 4))
print((2 < 3) or (3 < 4))

# & aur | bitwise operators hain; and/or logical operators hain.
print((2 < 3) & (3 < 4))
print((2 < 3) | (3 < 4))

# Bahut bada float exponent OverflowError de sakta hai.
# print(1.5 ** 1199)
print(1.5 ** 10)
