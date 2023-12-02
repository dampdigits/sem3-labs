# Write a program to input the marks of a student in 4 subjects, calculate the total aggregate and display the grades obtained by the student.

# marks > 90 -> O
# marks > 80 -> E
# marks > 70 -> A
# marks > 60 -> B
# marks > 50 -> C
# marks >= 40 -> D
# marks < 40 -> F

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

# Output:

# Enter the marks in the following subjects:

# Maths: 93
# Computer: 100
# Science: 95
# English: 96
# Grade: O