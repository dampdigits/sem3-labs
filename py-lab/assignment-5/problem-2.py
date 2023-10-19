# Program displays the following pattern
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

n = 6
for row in range(n):
    for col in range(n):
        if row > col:
            print(end=" ")
        else:
            print("*", end=" ")
    print()