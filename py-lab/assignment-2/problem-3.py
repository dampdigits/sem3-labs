item =input("Item: ")
quantity = int(input("Quantity: "))
costPrice = int(input("Cost price: "))
discountPercent = int(input("Discount %: "))
taxPercent = int(input("Tax %: "))

discount = costPrice * discountPercent / 100
discountedPrice = quantity * (costPrice - discount)
tax = discountedPrice * taxPercent / 100
billAmount = round(discountedPrice + tax)

print(f"\nBill amount of {quantity} {item} ₹{billAmount}")
