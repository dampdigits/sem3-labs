#     1 
#    2 2 
#   3 3 3 
#  4 4 4 4 
# 5 5 5 5 5 

for i in range(5):
    spaces = 5 - i - 1
    for j in range(5):
        if j <= spaces - 1:
            print(end = " ")
        else:
            print(f"{i + 1}", end = " ")
    print()
