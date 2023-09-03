# Write a program to enter numbers using while loop until -1 is encountered and count the number of prime and composite number.

primes = 0
composites = 0

while True:
    num = int(input("Number: "))

    if num == -1:
        break

    if num in (0, 1):
        continue
    # Check if prime or composite
    isPrime = True
    for index in range(2, int(num / 2)):
        if num % index == 0:
            composites += 1
            isPrime = False
            break
    if isPrime:
        primes += 1
print(f"prime numbers: {primes}, composite numbers: {composites}")

# ------------------------------------------
# OUTPUT:-
# Number: 5
# Number: 7
# Number: 6
# Number: 3
# Number: 1
# Number: 0
# Number: 2
# Number: -1
# prime numbers: 4, composite numbers: 1
