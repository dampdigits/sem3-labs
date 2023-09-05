# Write a python function that takes a number as a parameter and checks whether the number is prime or not.

def checkPrime(num):
    isPrime = True

    for index in range(2, int(num / 2)):
        if num % index == 0:
            isPrime = False
            break
    
    return isPrime

num = int(input("Number: "))
if checkPrime(num):
    print(f"Its a prime number")
else:
    print(f"Its not a prime number")

# ----------------------------------------------

# OUTPUT:-

# Number: 89
# Its a prime number
