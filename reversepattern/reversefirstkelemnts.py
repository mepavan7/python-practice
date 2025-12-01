'''Problem 5: Reverse First K Words

Given a sentence, reverse the first k words in every group of 2k words.

Example:
s = "I love coding and learning new things", k = 2
Words: ["I", "love", "coding", "and", "learning", "new", "things"]
First 2 reverse → "love I", next 2 keep → "coding and", next 2 reverse → "new learning", last → "things"
Output → "love I coding and new learning things"

Hint:
Use split() and then apply the same “2k” pattern — but with words instead of characters.'''



def reverse_first_k_elements(s, k):
    final_list = []
    words = s.split()
    for i in range(0, len(words), 2*k):
        first_block = words[i:i+k]
        second_block = words[i+k:i+2*k]
        final_list.extend(first_block[::-1])
        final_list.extend(second_block)
    return " ".join(final_list)
print(reverse_first_k_elements("I love coding and learning new things", 2))

 #flat = [item for sub in final_list for item in sub]