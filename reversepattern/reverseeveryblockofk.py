'''Problem 3: Reverse Every 3rd Block of K

Given string s and integer k,
for every 3rd block of k characters, reverse it; otherwise, keep as-is.

Example:
s = "abcdefghijkl", k = 2
→ ab cd ef gh ij kl
Reverse only 3rd, 6th, 9th... block →
ab cd fe gh ij kl → abcdfeghijkl

Hint:
You’ll need a block counter (count = 1, 2, 3, ...) and condition (if count % 3 == 0).'''

# i used string (concatination)
def reverse_every_block_k(s, k):
    count = 0
    rev = ''
    for i in range(0, len(s), k):
        t = s[i:i+k]
        count += 1 
        if (count % 3 == 0):
            rev += t[::-1]
        else:
            rev += t
    return rev
print(reverse_every_block_k("abcdefghijkl", 2))

# now i am usinf here list
def reverse_every_block_k(s, k):
    count = 0
    parts = []
    for i in range(0, len(s), k):
        block = s[i:i+k]
        count += 1
        if count % 3 == 0:
            parts.append(block[::-1])
        else:
            parts.append(block)
    return "".join(parts)
print(reverse_every_block_k("abcdefghijkl", 2))

    
