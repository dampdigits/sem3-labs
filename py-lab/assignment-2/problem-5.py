# A company decides to give bonus to all it's employees on Diwali. A 5% bonus on salary is given to the male workers 10% bonus on salary to the female workers.
# Write a program to input the salary and sex of the employee. If the salary of the employee is less than ₹10,000 then the employee gets an extra 2% bonus on salary. Calculate the bonus that has to be given to the employee and display the salary that the employee will get.

salary = int(input("Salary: "))
sex = input("Sex: ")

if sex.lower() == "male":
    bonusPercent = 5
else:
    bonusPercent = 10

if salary < 10000:
    bonusPercent += 2

salary = round(salary + (salary * bonusPercent / 100))

print(f"Final salary: ₹{salary}")
