# Write a program to display the fibonacci series

number = int(input("Number: "))
a = 0
b = 1
sum = a + b

print(f"{a} {b}", end=" ")

for index in range(number):
    print(sum, end=" ")
    a, b = b, sum
    sum = a + b
print()

# Output:
# Number: 10
# 0 1 1 2 3 5 8 13 21 34 55 89
