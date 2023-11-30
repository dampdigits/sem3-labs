# Write a program to calculate the total amount of money in a piggybank. Coins: ₹1, ₹2, ₹5, ₹10

print("Enter the number coins of:")

coins10 = int(input("₹ 10: "))
coins5 = int(input("₹ 5: "))
coins2 = int(input("₹ 2: "))
coins1 = int(input("₹ 1: "))

money = (10 * coins10) + (5 * coins5) + (2 * coins2) + (1 * coins1)

print(f"Money: {money}")

# Output:
# Enter the number coins of:
# ₹ 10: 5
# ₹ 5: 6
# ₹ 2: 2
# ₹ 1: 0
# Money: 84