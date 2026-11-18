# Lambda Functions - Arguments

# Lambda ek se zyada arguments bhi le sakta hai.
add = lambda first, second: first + second
print(add(6, 7))

# Default argument bhi de sakte hain.
add_default = lambda first, second=20: first + second
print(add_default(30))
print(add_default(30, 5))

# Conditional expression ke saath lambda.
# Negative number ke liye 0, warna number ka square.
safe_square = lambda number: 0 if number < 0 else number * number
print(safe_square(-5))
print(safe_square(5))

# Complex logic ke liye def function zyada readable hota hai.
