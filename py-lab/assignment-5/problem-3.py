# Program displays the following pattern
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

n = 5
for row in range(n):
    for col in range(n):
        if row + col < n - 1:
            print(end=" ")
        else:
            print("*", end=" ")
    print()