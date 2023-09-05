# Write a python function that accepts a string and counts the number of upper and lower case letters.

def countLetterCase(string):
    global uppers
    global lowers
    uppers = 0
    lowers = 0

    for ch in string:
        if ch.isupper():
            uppers += 1
        if ch.islower():
            lowers += 1

string = input("String: ")
countLetterCase(string)

print(f"No. of uppercase letters: {uppers}")
print(f"No. of lowercase letters: {lowers}")

# ---------------------------------------------------

# OUTPUT:-

# String: Hello World!
# No. of uppercase letters: 2
# No. of lowercase letters: 8
