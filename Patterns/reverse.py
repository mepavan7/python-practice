n = int(input())
for i in range(n+1):
    for j in range(1, n-i+1):
        print(j, end="")
    print()
    

n = int(input())
i = 0
while i < n+1:
    j = 1
    while j < n-i+1:
        print(j, end="")
        j += 1
    i += 1
    print()
