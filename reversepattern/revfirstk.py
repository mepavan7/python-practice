'''Problem 1: Reverse First K (Variation 1)

Given a string s and integer k,
reverse every alternate block of k characters.

Example:
s = "abcdefgh", k = 3
👉 First 3 reverse → cba, next 3 keep → def, next 2 reverse → hg
Output → cbadefhg'''

def reverse_of_first_k(s, k):
    L = len(s)
    res = ""
    for i in range(0, L, 2*k):
        t = s[i:i+k]
        t1 = s[i+k:i+2*k]
        res += t[::-1] + t1
    return res
print(reverse_of_first_k("abcdefgh", 3))