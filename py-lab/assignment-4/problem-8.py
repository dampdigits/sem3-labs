# Write a python function that takes a list and returns a new list with distinct elements from the first list.

def distinctList(oldList):
    newList = []
    for element in oldList:
        if element not in newList:
            newList.append(element)
    return newList

oldList = []

while True:
    element = input("Element: ")
    if element == "":
        break
    oldList.append(element)

newList = distinctList(oldList)

print(newList)

# --------------------------------------------------------

# OUTPUT:-

# Element: 89
# Element: too-Easy
# Element: 404
# Element: Not Found!
# Element: too-Easy
# Element: 404
# Element: 
# ['89', 'too-Easy', '404', 'Not Found!']
