# Write a python function to multiply all the numbers in a list.

def product_list(num_list):
    product = 1
    for number in num_list:
        product *= number
    return product

num_list = [8, 2, 3, -1, 7]
print(f"List: {num_list}")

product = product_list(num_list)
print(f"Product of the numbers in the list is {product}")

# --------------------------------------------------------

# OUTPUT:-

# List: [8, 2, 3, -1, 7]
# Product of the numbers in the list is -336
