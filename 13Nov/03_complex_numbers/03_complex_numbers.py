# 13 Nov: Complex Numbers

# Complex number ka format real + imaginary*j hota hai.
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

# Complex numbers par < aur > comparison supported nahi hota.
# print(complex_number > other_complex)  # TypeError

# Parentheses ka dhyan rakhein:
print(-1 ** 0.5)  # -(1 ** 0.5), result -1.0
print((-1) ** 0.5)  # Parentheses ki wajah se complex result
