number = int(input("Number: "))
factorial = 1

for index in range(1 , number + 1):
    factorial *= index

print(f"Factorial: {factorial}")
