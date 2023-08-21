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
