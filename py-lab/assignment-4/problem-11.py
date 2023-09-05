# Write a python function to check whether a number is "Perfect" or not.

def isPerfect(num):
    aliquotSum = 0

    for i in range(1, int(num / 2 + 1)):
        if num % i == 0:
            aliquotSum += i

    return aliquotSum == num

num = int(input("Number: "))
if isPerfect(num):
    print("Its a perfect number")
else:
    print("Its not a perfect number")

# ----------------------------------------------

# OUTPUT:-

# Number: 8128
# Its a perfect number
