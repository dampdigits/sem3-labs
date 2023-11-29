# Write a program to check if a number is an armstrong number
# Armstrong number is the number in any given number base, which forms the total of the same number, when each of its digits is raised to the power of the number of digits in the number.
# Eg. 153 and 370

num = input("Number: ")
digitCount = len(num)
num = int(num)
sum = 0
tmp = num

for index in range(digitCount):
    digit = tmp % 10
    sum += pow(digit, digitCount)
    tmp = int(tmp / 10)

if sum == num:
    print("Its an armstrong number")
else:
    print("Its not an armstrong number")

# Output:

# Number: 191
# Its not an armstrong number