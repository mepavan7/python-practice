rows = 4 
cols = 5
for r in range(1, rows+1):
    for c in range(1, cols+1):
        if r == 1 or r == rows or c == 1 or c == cols:
            print("*", end="")
        else:
            print(" ", end="")
    print()