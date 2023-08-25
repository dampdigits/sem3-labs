# Write a program to check if a number is an armstrong number

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
