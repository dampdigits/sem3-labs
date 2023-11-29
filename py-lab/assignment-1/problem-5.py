# Write a program to find the numbers between 0 and 100 which are divisible by 7 but not by 5

for index in range(100):
    if (index % 7 == 0) and (index % 5 != 0):
        print(index, end=" ")
print()

# Output:
# 7 14 21 28 42 49 56 63 77 84 91 98 