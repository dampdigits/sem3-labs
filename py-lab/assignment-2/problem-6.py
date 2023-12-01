# Write a program to check whether a character is a vowel or a consonant.

letter = input("Character: ").lower()

if letter in ('a', 'e', 'i', 'o', 'u'):
    print("It is a vowel.")
else:
    print("It is a consonant.")

# Output:
# Character: k
# It is a consonant.