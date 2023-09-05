# Write a python function to check whether a number falls within a given range.

def check(num, limit):
    found = False
    for i in range(limit + 1):
        if i == num:
            found = True
            break
    return found

num = int(input("Search-number: "))
limit = int(input("Range: "))

if check(num, limit):
    print(f"Yes {num} lies within the range of {limit}")
else:
    print(f"No {num} doesn't lies within the range of {limit}")

# ---------------------------------------------------------------------------

# OUTPUT:-

# Search-number: 85
# Range: 120
# Yes 85 lies within the range of 120
