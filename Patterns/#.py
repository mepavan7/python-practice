n = int(input())
for i in range(n):
    star = 2*i+1
    space = n-i-1
    print((" "*space)+(star*"#"))
for j in range(n-2, -1, -1):
    star = 2*j+1
    space = n-j-1
    print((" "*space)+(star*"#"))


    