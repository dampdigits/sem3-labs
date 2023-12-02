# Write a program to calculate the factorial of a number.

number = int(input("Number: "))
factorial = 1

for index in range(1 , number + 1):
    factorial *= index

print(f"Factorial: {factorial}")

# Output:
# Number: 8
# Factorial: 40320