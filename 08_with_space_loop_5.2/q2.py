#         5
#       4 5
#     3 4 5
#   2 3 4 5
# 1 2 3 4 5


for i in range(5, 0):
    for s in range(i - 1):
        print(" ", end=" ")
    for j in range(i, 6):
        print(j, end=" ")
    print()
