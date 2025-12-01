'''Problem 2: Reverse Alternate K (Right to Left)

Given a string s and integer k,
start from the end of the string and apply the same rule:
reverse last k, skip next k, and move leftward.

Example:
s = "abcdefgh", k = 2
Work from right:
gh → reverse → hg, skip ef, reverse cd → dc, skip ab.
Output → abdc ef hg → abdcefhg

Hint:
Use slicing in reverse order. Try using negative indices'''

def reverse_alternate_k(s, k):
    #final_res = []
    res = ""
    for i in range(len(s), 0,-(2*k)):
        '''right_part = s[i-k : i]
        left_part = s[i-2*k : i-k]'''
        left_start = max(0, i-2*k)
        mid_start = max(0, i-k)
        left_part = s[left_start:mid_start]
        right_part = s[mid_start:i]
        res =  (left_part + right_part[::-1]) + res
        '''final_res.append(res)
        final = "".join(final_res)
        '''
    return  res
#print(reverse_alternate_k("abcdefgh", 2))
#print(reverse_alternate_k("abcdefghij", 2))
#print(reverse_alternate_k("abcdefghi", 2))

def reverse_alternate_k(s):
    left = 0
    right = len(s) - 1
    res = ""
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
#print(reverse_alternate_k("abcdefgh"))
#print(reverse_alternate_k("racecar"))

def reverse_alternate_k(s, k):
    #final_res = []
    res = ""
    for i in range(len(s), 0,-(2*k)):
        '''right_part = s[i-k : i]
        left_part = s[i-2*k : i-k]'''
        left_start = max(0, i-2*k)
        mid_start = max(0, i-k)
        left_part = s[left_start:mid_start]
        right_part = s[mid_start:i]
        res =  (left_part + right_part[::-1]) + res
        #final_res.extend(left_part)
        #final_res.extend(right_part[::-1])
        '''final_res.append(res)
        final = "".join(final_res)
        '''
    return  res
print(reverse_alternate_k("abcdefgh", 2))
print(reverse_alternate_k("abcdefghij", 2))
print(reverse_alternate_k("abcdefghi", 2))


