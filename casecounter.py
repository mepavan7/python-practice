'''Write a function that counts the number of uppercase and lowercase letters in a string.

Function Description Complete the count_cases function.

count_cases has the following parameter:

s (string): The string to be analyzed.

Prints

The function should print two lines (it should not return anything):

Uppercase: [count]

Lowercase: [count]

(Note: Ignore spaces and punctuation)

Sample Input

Hello World!
Sample Output (from the function itself)

Uppercase: 2
Lowercase: 8
'''
def character_count(s):
    lower_count = 0
    upper_count = 0
    for i in range(len(s)):
        lower_count += s[i].islower()
        upper_count += s[i].isupper()
    print(upper_count)
    print(lower_count)
    #return lower_count, upper_count
print(character_count("Hello World"))