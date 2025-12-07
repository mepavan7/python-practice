# # row = 4
# # cols = 5
# # for r in range(1, row+1):
# #     for c in range(1, cols+1):
# #         if r == 1 or r == row or c == 1 or c == cols:
# #             print("*", end="")
# #         else:
# #             print(" ", end="")
# #     print()
            
# row = 4
# cols = 5
# r = 1
# while r < row+1:
#     c = 1
#     while c < cols+1:
#             if r == 1 or r == row or c == 1 or c == cols:
#                 print("*", end="")
#             else:
#                 print(" ", end="") 
#             c += 1
#     r += 1
#     print()

n = int(input())
for i in range(n):
    pat = 2*i+1
    space = n-i
    print(" " * space, end="")
    for j in range(n-i+1):
        if i == 1 or  i == n:
         print("*", end="")
    print()