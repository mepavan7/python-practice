# n = int(input())
# for i in range(n+1):
#     for j in range(1, n-i+1):
#         print(" "*(n-i) , j, end="")
#     print()
    

n = int(input())
for i in range(n+1):
    spaces = n-i
    print(" a" * spaces, end="") 
    for j in range(1, i+1):
        print(j, end="")
        
    print()

n = int(input())
for i in range(n+1):
    print(" "* (n-i), end="")
    for j in range(1, i+1):
        print(j, end="")
    print()
