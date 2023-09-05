# Write a python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

def sortWords():
    sequence = input("Hyphen separated equence: ")
    words = sequence.split("-")
    words.sort()
    sortedSequence = ""
    for word in words:
        if word == words[-1]:
            sortedSequence = sortedSequence + word
        else:
            sortedSequence = sortedSequence + word + "-"
    
    print(f"Sorted sequence: {sortedSequence}")

sortWords()

# ------------------------------------------------

# OUTPUT:-

# Hyphen separated equence: green-red-yellow-black-white
# Sorted sequence: black-green-red-white-yellow
