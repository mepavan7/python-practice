def string_filter(s, k):
    L = len(s)
    res = []
    for i in range(0, L, k):
        t = s[i:i+k]
        #res.append(t)
        if len(t) < k:
            #t += "x"
            m = k - len(t)
            for j in range(m):
                t += 'x'
            res.append(t)
        else:
            res.append(t)
        
    return res
print(string_filter("abcdefgh", 3))   
#print(string_filter("abcdefghi", 3))   
print(string_filter("a", 5))   

#so here i use for loop add m times string but very slow for that reason time complexsity also more, we can do like this t = 'x' * m
def string_filter(s, k):
    L = len(s)
    res = []
    for i in range(0, L, k):
        t = s[i:i+k]
        #res.append(t)
        if len(t) < k:
            #t += "x"
            m = k - len(t)
            t += 'x'*m
            res.append(t)
        else:
            res.append(t)
        
    return res
print(string_filter("abcdefgh", 3))   
#print(string_filter("abcdefghi", 3))   
print(string_filter("a", 5))   
