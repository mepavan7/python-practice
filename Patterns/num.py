n = int(input())
for i in range(n):
    print(" "*(n-i-1), end="")#space
    #asscending order 
    for j in range(1, i+2):
        print(j, end="")
    #Desscending order
    for k in range(i, 0, -1):
        print(k, end="")
    print()
for i in range(n-2, -1, -1):
    print(" "*(n-i-1), end="")
    for j in range(1, i+2):
        print(j, end="")
    for k in range(i, 0, -1):
        print(k, end="")
    print()
        
        