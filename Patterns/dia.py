n = int(input())
#upper part
for i in range(n):
    star = 2*i+1
    space = n-i+1
    print((" "*space) + (star*"*"))
#lower part
for i in range(n-2, -1, -1):
    star = 2*i+1
    space = n-i+1
    print((" "*space) + (star*"*"))
    