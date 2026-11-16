# Sets - Hinglish Notes

# Set unordered collection hai aur duplicate values store nahi karta.
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

print(type(s1))

# union: dono sets ke unique elements.
print(s1.union(s2))
print(s1 | s2)

# intersection: common elements.
print(s1.intersection(s2))
print(s1 & s2)

# difference: pehle set mein hain, doosre mein nahi.
print(s1 - s2)

# Tuple ko set mein convert karna.
tp = (1, 2, 3, 4, 5)
sp = set(tp)
print(sp)

# Set mutable hota hai, isliye uski identity dekh sakte hain.
print(id(sp))

# Empty set banane ke liye set() use karein; {} empty dictionary hota hai.
empty_set = set()
print(type(empty_set))
