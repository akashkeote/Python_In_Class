# Lambda Functions - Basic Notes

# Lambda ek chhota, anonymous function hota hai.
# Anonymous ka matlab hai ki function ka formal naam zaroori nahi hota.
# Lambda ka use short aur simple operation ke liye hota hai.

# Syntax:
# lambda arguments: expression

# Normal function:
def square_normal(number):
    return number * number


# Same kaam lambda se:
square = lambda number: number * number

print(square_normal(5))
print(square(5))

# Lambda ko direct bhi call kar sakte hain.
print((lambda number: number * number)(6))
