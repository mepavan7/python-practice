''''Problem 4: Reverse K, Skip M

Given a string s and integers k and m,
reverse first k characters, skip next m, repeat.

Example:
s = "abcdefghij", k = 2, m = 3

Reverse ab → ba, skip cde, reverse fg → gf, skip hij
Output → bacdegfhij

Hint:
Step size = k + m.'''



def reverse_k_skip_m(s, k , m):
    first_list = []
    #rev = ''
    for i in range(0, len(s), k+m):
        skip_block = s[i+k:i+k+m]
        reverse_block = s[i:i+k]
        first_list.append(reverse_block[::-1])
        #rev += block
        first_list.append(skip_block)  
    return "".join(first_list)
print(reverse_k_skip_m("abcdefghij", 2, 3))
print(reverse_k_skip_m("abcdefg", 3, 2))