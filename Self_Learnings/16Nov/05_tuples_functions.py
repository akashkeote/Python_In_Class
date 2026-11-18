# Tuples aur Functions - Hinglish Notes

# Tuple ordered hota hai, lekin immutable hota hai.
t1 = (1, 2, 3, 4)
print(t1)
print(type(t1))
print(t1[0])
print(t1[1:3])

# Tuple unpacking: values variables mein assign hoti hain.
x, y, z, t = t1
print(x, y, z, t)

# t1[0] = 100  # Error: tuple immutable hai

# Function multiple values return kar sakta hai.
def calculate(a, b):
    return a + b, a - b, a * b, a // b

result = calculate(10, 5)
print(result)

addition, subtraction, multiplication, division = calculate(10, 5)
print(addition)
print(subtraction)
print(multiplication)
print(division)
