# Write a program to display the fibonacci series

number = int(input("Number: "))
a = 0
b = 1
sum = a + b

print(f"{a}\t{b}", end="\t")

for index in range(number):
    print(sum, end="\t")
    a, b = b, sum
    sum = a + b
print()
