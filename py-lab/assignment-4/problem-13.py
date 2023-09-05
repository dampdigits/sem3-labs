# Write a python function that prints out the first n rows of Pascal's triangle.

def pascalTriangle(num):
    for row in range(num):
        print(" " * (num - row - 1), end="")
        for col in range(row + 1):
            # n C r = row C col
            n, r = 1, 1

            for i, j in zip(range(row, row - col, -1), range(col, 0, -1)):
                n *= i
                r *= j
            
            print(int(n/r), end=" ")
        print()

num = int(input("Number of rows: "))
pascalTriangle(num)

# -----------------------------------------------

# OUTPUT:-

# Number of rows: 5
#     1 
#    1 1 
#   1 2 1 
#  1 3 3 1 
# 1 4 6 4 1 
