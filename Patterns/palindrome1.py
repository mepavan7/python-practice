n = int(input())
for i in range(n+1):
    print(" "*(n-i+1), end="")
    for j in range(1, i):
        print(j, end="")
    for k in range(i, 0, -1):
        print(k, end="")
    print()
    
n = int(input())
i = 0
while i<=n:
    print(" " *(n-i), end="")
    j = 1
    while j <= i:
        print(j, end="")
        j += 1
    k = i-1
    while k > 0:
        print(k, end="")
        k -= 1
    i += 1
    print()