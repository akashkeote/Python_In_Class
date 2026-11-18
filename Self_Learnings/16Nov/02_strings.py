# Strings - Hinglish Notes

s1 = "hello world"

# Check karna ki string kis text se start ya end hoti hai.
print(s1.startswith("j"))
print(s1.endswith("ay"))

# String ko repeat karna.
s2 = s1 * 2
print(s2)

# split() string ko list mein todta hai.
print(s2.split(sep="o"))
print(s2.split())

# join() list ke words ko ek string mein jodta hai.
print("$".join(s2.split()))
print("akash".join(s2.split()))

# replace() purane text ko naye text se replace karta hai.
print(s1.replace("l", "a"))

# Strings immutable hoti hain: original string directly change nahi hoti.
