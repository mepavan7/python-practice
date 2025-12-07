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
            