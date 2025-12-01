#Method 1: The "Backward Range"
def reverse_string(str):
    rev = ''
    for i in range(len(str)-1, -1, -1):
        rev += str[i]
    return rev
print(reverse_string("python"))

#Method 2: The "Forward Loop, Backward Build"
def reverse_string(str):
    rev = ''
    for i in range(len(str)):
        rev = str[i] + rev
    return rev
print(reverse_string("python"))

#method 3
def reverse_string(s):
    s = list(s)
    l, r = 0, len(s)-1
    while l < r:
        s[l],s[r] = s[r],s[l]
        l += 1
        r -= 1
    return "".join(s)
print(reverse_string("python"))