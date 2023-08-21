print("Enter the marks in the following subjects:\n")

maths = int(input("Maths: "))
computer = int(input("Computer: "))
science = int(input("Science: "))
english = int(input("English: "))

averageMarks = round((maths + computer + science + english) / 4)

if averageMarks > 90:
    grade = 'O'
elif averageMarks > 80:
    grade = 'E'
elif averageMarks > 70:
    grade = 'A'
elif averageMarks > 60:
    grade = 'B'
elif averageMarks > 50:
    grade = 'C'
elif averageMarks >= 40:
    grade = 'D'
else:
    grade = 'F'

print(f"Grade: {grade}")
