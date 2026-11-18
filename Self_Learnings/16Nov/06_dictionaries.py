# Dictionaries - Hinglish Notes

# Dictionary key-value pairs store karta hai.
emp = {
    "name": "akash",
    "age": 25,
    "city": "Mumbai",
    "projects": ["project1", "project2", "project3"],
}

print(type(emp))
print(emp["projects"])

# in dictionary mein keys check karta hai, values nahi.
print("projects1" in emp)
print("projects" in emp)

# Ye view objects return karte hain.
print(emp.keys())
print(emp.values())
print(emp.items())

# Existing value update karna.
emp["name"] = "jay"
print(emp)

# popitem() last inserted key-value pair remove karta hai.
removed_item = emp.popitem()
print(removed_item)
print(emp)

# update() dictionaries merge karta hai.
d1 = {1: 2, 2: 3, 3: 4}
d2 = {4: 5, 5: 6, 6: 7}
d1.update(d2)
print(d1)

# Duplicate keys allowed nahi hoti; last value save hoti hai.
duplicate_keys = {1: 3, 1: 6, 1: 9}
print(duplicate_keys)  # {1: 9}

# Mutable list dictionary key nahi ban sakti, kyunki list unhashable hai.
# invalid = {[1, 2, 3]: "value"}

stringdict = {
    "name": "akash",
    "age": 25,
    "city": "Mumbai",
    "projects": ["project1", "project2", "project3"],
}
print(stringdict["projects"][0])
print(stringdict["city"])
