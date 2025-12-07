n = int(input())
for i in range(n):
    # spaces
    print(" "*(n-i-1), end="")
    # ascending numbers
    for j in range(1, i+2):
        print(j, end="")
     # descending numbers
    for k in range(i, 0, -1):
        print(k, end="")
    print()
    