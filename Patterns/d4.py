n = int(input())
#Upper half 
for i in range(n):
    #space
    print("a " *(n-i), end="")
    #Ascending order
    for j in range(1, i+1):
        print(j, end="")
    #Decending orsder
    for k in range(i+1, 0, -1):
        print(k, end="")
    print()
#lower part
for i in range(n-1, -1, -1):
    print(" " *(n-i+1), end="")
    for j in range(1, i+1):
        print(j, end="")
    #Decending orsder
    for k in range(i-1, 0, -1):
        print(k, end="")
    print()
    
n = int(input())    
i = 0
#Upper half 
while i < n:
     #space
    print(" " *(n-i), end="")
    #Ascending order
    j = 1
    while j < i+1:
        print(j , end="")
        j += 1
    #Decending orsder
    k = i+1 
    while k > 0:
        print(k ,end="")
        k -= 1
    i += 1
    print()
 #lower part
i = n-1
while i > -1:
       print(" " *(n-i+1), end="")
       j = 1
       while j < i+1:
           print(j, end="")   
           j += 1
       k = i - 1
       while k > 0:
           print(k, end="")
           k-= 1
       i -= 1
       print()
            