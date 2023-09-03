# Write a Python Program to print the sum of the series :  1/(2^1) + 1/(2^2) + ... + 1/(2^n)

sum = 0
n = int(input("Limit: "))

for index in range(1, n + 1):
    sum += 1 / (2 ** index)

print(f"Sum of the series: {sum}")

# ---------------------------------------------
# OUTPUT:-
# Limit: 5
# Sum of the series: 0.96875
