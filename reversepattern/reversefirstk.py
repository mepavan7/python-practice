s = 'abcdefg'
k = 2
L = len(s)
final_rev = ''
for i in range(0,L,k*2):
    '''t = s[i:i+k+2]
    rev = t[0:2]
    rev = rev[::-1]
    final_rev +=  rev + t[i+2:k+2]
    '''
    t = s[i:i+k] 
    rev = t[::-1]
    withoutrev = s[i+k:i+k*2]
    final_rev += (rev) + (withoutrev)
print(final_rev)