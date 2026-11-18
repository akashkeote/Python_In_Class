# 13 Nov: Slicing aur String Methods

# Slicing ka format sequence[start:stop:step] hota hai.
# start included hota hai, stop excluded hota hai.
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])  # [1, 2, 3]
print(numbers[::2])  # Har second element.
print(numbers[1::2])  # Index 1 se har second element.
print(numbers[::-1])  # Reverse list.

s2 = "hello world"
print(s2)
print(s2.center(50, "X"))  # String ko center mein place karta hai.
print(s2.split())  # Words ki list banata hai.
print(s2.find("o"))  # First match ka index, nahi mile to -1.
print(s2.index("o"))  # First match ka index, nahi mile to error.
print(s2[s2.find("h")])

# dir() object ke available attributes aur methods dikhata hai.
print(dir(s2))
