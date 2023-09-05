# Write a python function to check whether a string is a pangram or not
from string import ascii_lowercase

def isPangram(string):
    lowercase_letters = list(ascii_lowercase)
    for letter in lowercase_letters:
        if (letter not in string) and (letter.upper() not in string):
            return False
    return True

string = input("String: ")
if isPangram(string):
    print(f"Its a pangram.")
else:
    print(f"Its not a pangram.")

# -----------------------------------

# OUTPUT:-

# String: The quick brown fox jumps over the lazy dog
# Its a pangram
