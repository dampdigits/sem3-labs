# Write a python function to calculate the factorial of a non-negative integer.

def factorial(number):
    factorial = 1

    for index in range(1 , number + 1):
        factorial *= index

    return factorial

number = int(input("Number: "))
fact = factorial(number)
print(f"Factorial: {fact}")

# --------------------------------------------------------

# OUTPUT:-

# Number: 5
# Factorial: 120
