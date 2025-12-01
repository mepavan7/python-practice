s = 'ABCDCDC'
ss = 'CDC'
count = 0
for i in range(len(s)):
    slice = s[i:i+len(ss)] 
    print(slice)
    if slice == ss:
        count += 1
print(count)
        