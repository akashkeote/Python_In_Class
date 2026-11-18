# Lambda Functions - map() aur filter()

numbers = [1, 2, 3, 4, 5]

# map() har item par function apply karta hai.
squares = map(lambda number: number * number, numbers)
print(list(squares))

# filter() sirf un items ko select karta hai jinke liye condition True ho.
even_numbers = filter(lambda number: number % 2 == 0, numbers)
print(list(even_numbers))

# map() aur filter() result mein iterator dete hain.
# Isliye output dekhne ke liye list() use kar sakte hain.

# Same kaam def function ke saath bhi kar sakte hain.
def square(number):
    return number * number

print(list(map(square, numbers)))
