# Write a program to display the following sequence: 1 2 3 4 5 6 .... n

limit = int(input("Number-limit: "))
for index in range(1, limit + 1):
    print(index, end=" ")
print()

# Output:
# Number-limit: 10
# 1 2 3 4 5 6 7 8 9 10 