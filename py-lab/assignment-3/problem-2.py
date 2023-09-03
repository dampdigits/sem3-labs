# Write a Python Program to print the sum of the series :  1/(2*2) + 1/(3*3) + ... + 1/(n*n)

sum = 0
n = int(input("Limit: "))

for index in range(2, n + 1):
    sum += 1 / (index * index)

print(f"Sum of the series: {sum}")

# -------------------------------------------
# OUTPUT:-
# Limit: 5
# Sum of the series: 0.4636111111111111
