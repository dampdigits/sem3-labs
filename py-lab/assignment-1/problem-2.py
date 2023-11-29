# Write a program to calculate the salary of an employee

bs = int(input("Base salary: ₹"))
hra = 0.05
da = 0.2
ma = 0.01
pf = 0.02
ts = bs + (bs * (hra + da + ma + pf))
print(f"Total salary: ₹{ts}")

# Output:
# Base salary: ₹50000
# Total salary: ₹64000.0