N, M = map(int, input().split())

for i in range(N//2):
    s = ((2*i)+1) * ".|."
    print(s.center(M, "-"))
print("WELCOME".center(M, "-"))
for i in range(N//2-1,-1,-1):
    s = ((2*i)+1) * ".|."
    print(s.center(M, "-"))
#If the two numbers are given on one line (e.g. 9 27) do this:
#N, M = map(int, input().split())

