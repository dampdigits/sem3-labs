# Write a python program to reverse a string.

def reverse(string):
    rev = string[::-1]
    return rev

string = input("String: ")
rev = reverse(string)
print(f"The reverse of {string} is {rev}")

# --------------------------------------------------------

# OUTPUT:-

# String: Avada Kedavra
# The reverse of Avada Kedavra is arvadeK adavA
