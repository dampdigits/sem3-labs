# Write a python program to print the even numbers from a given list.

def printEvens(numList):
    evenList = []
    for element in numList:
        if element % 2 == 0:
            evenList.append(element)
    
    return evenList

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"List: {numList}")
evenList = printEvens(numList)
print(f"List of even numbers: {evenList}")

# ----------------------------------------------------

# OUTPUT:-

# List: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# List of even numbers: [2, 4, 6, 8]
