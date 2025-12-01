def swapCase(s):
    container = ""
    for i in s:
        if i == i.lower():
            upper =  i.upper()
            container += upper
        elif i == i.upper():
            lower  = i.lower()
            container += lower
    return container
print(swapCase("HackerRank.com"))

def swapCase(s):
    result = ""
    for ch in s:
        if ch.islower():
            result += ch.upper()
        elif ch.isupper():
            result += ch.lower()
    return result
print(swapCase("hACKERrANK.COM PRESENTS pYTHONIST 2.")) 

a = 6
b = 5
temp = a
a = b
b = temp
print(a, b)
a = 34
b = 21
a, b = b, a
print(a, b)