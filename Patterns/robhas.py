
# x = 1
# while x <= 15:
#     if x % 2 != 0:
#         print(x)  
#     else:
#         print(x)
#     x += 1  
    
    
n = 5
for i in range(n):
    pat = 2*i+1
    space = n-i-1
    print((" " * space)+(pat*'*'))
for i in range(n-2, -1, -1):
    pat = 2*i+1
    space = n-i-1
    print((" " * space)+(pat*'*'))