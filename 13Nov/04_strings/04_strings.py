# 13 Nov: Strings

# String text ka sequence hoti hai aur immutable hoti hai.
c1 = "hello"
c2 = "hello"
print(c1 + c2)
print(c1 == c2)

# Multiline string triple quotes se banti hai.
paragraph = """this is
para
graph"""
print(paragraph)

# Raw string backslash ko escape nahi karti.
file_path = r"C:\Users\akash.keote\Desktop\python\sample.txt"
print(file_path)

s = "akash keote"
print(s[6])  # Index 6 ka character.

# isinstance se type check karte hain.
print(isinstance(s, str))

# Old-style formatting.
price_text = "the price of %s is %f for %d items"
print(price_text % ("apple", 5.5, 2))

# Modern f-string formatting.
print(f"the price of apple is {5.5:.2f} for {2} items")
