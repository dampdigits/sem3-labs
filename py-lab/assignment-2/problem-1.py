# Write a program to swap two numbers using a third variable and without using a third variable

# Using 3rd variable
a = 10
b = 20
print(f"\nBefore swap\na: {a}, b: {b}")
# swap
c = a
a = b
b = c

print(f"\nAfter swap\a: {a}, b: {b}")

# Without using 3rd variable
d = 52
e = 36
print(f"\nBefore swap\nd: {d}, e: {e}")
# swap
d, e = e, d

print(f"\nAfter swap\d: {d}, e: {e}")

# Output:
# 1.py

# Before swap
# a: 10, b: 20

# After swap: 20, b: 10

# Before swap
# d: 52, e: 36

# After swap\d: 36, e: 52