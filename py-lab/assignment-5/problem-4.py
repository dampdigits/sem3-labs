# Program displays the following pattern
# * 
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

n = 20
top = int(n/2)
bottom = n - top
for row in range(1, top + 1):
    print("* " * row)
for row in range(bottom, 0, -1):
    print("* " * row)