# Write a Python function to sum all the numbers in a list.

def sum_list(num_list):
    sum = 0
    for number in num_list:
        sum += number
    return sum

num_list = [8, 2, 3, 0, 7]
print(f"List: {num_list}")

sum = sum_list(num_list)
print(f"Sum of the numbers in the list is {sum}")

# --------------------------------------------------------

# OUTPUT:-

# List: [8, 2, 3, 0, 7]
# Sum of the numbers in the list is 20
