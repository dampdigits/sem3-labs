# Write a python function that checks whether a passed string is a palindrome or not.

def isPalindrome(string):
    reverse = string[::-1]
    return reverse == string

string = input("String: ")
if isPalindrome(string):
    print("Its a palindrome.")
else:
    print("Its not a palindrome.")

# ------------------------------------------

# OUTPUT:-

# String: mom
# Its a palindrome.
