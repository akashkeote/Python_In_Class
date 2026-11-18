# Lists - Hinglish Notes

# List ordered aur mutable collection hoti hai.
x1 = [1, 2.5, 1 + 2j, "abc"]
print(x1)
print(type(x1))
print(x1[0])
print(x1[1:3])

# List ke elements ko change kar sakte hain.
x1[0] = 100
print(x1)

# append() end mein item add karta hai.
x1.append(1000)
print(x1)

# pop() item remove karke return karta hai.
print(x1.pop())
print(x1.pop(0))

# reverse() list ko in-place reverse karta hai aur None return karta hai.
x1.reverse()
print(x1)

# Slicing se reversed copy milti hai.
print(x1[::-1])

# sort() numbers ko ascending order mein arrange karta hai.
x3 = [745, 4, 6, 3, 2, 1, 0]
x3.sort()
print(x3)

# Useful methods.
x3.append(8)
print(x3.index(4))
print(len(x3))

# in membership check karta hai.
print(8 in x3)
