n = int(input())
#Part A: The Upper Triangle
for i in range(n):
    print(" " * (n-i-1), end="")
    print("*", end="")
    if i == 0:
        print()
    else:
        s = 2*i-1
        print(" "*s, end="")
        print("*")
        print(end="")
#Part B: The Lower Triangle
for i in range(n-2, -1, -1):
    print(" " * (n-i-1), end="")
    print("*", end="")
    if i == 0:
        print()
    else:
        s = 2*i-1
        print(" "*s, end="")
        print("*")
        print(end="")
  