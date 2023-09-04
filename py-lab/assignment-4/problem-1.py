# Write a python function to find the maximum of three numbers.

def max(a, b, c):
    maximum = a
    for number in (b, c):
        if maximum < number:
            maximum = number
    return maximum

a = int(input("Number-1: "))
b = int(input("Number-1: "))
c = int(input("Number-1: "))

maximum = max(a, b, c)
print(f"The maximum of these three numbers is {maximum}")

# --------------------------------------------------------

# OUTPUT:-

# Number-1: 5
# Number-1: 4899
# Number-1: -0
# The maximum of these three numbers is 4899
