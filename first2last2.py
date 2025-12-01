'''First Two, Last Two
Your Task: Get a new string made of the first 2 and last 2 characters of an existing string.

Function Description Complete the get_first_last function.

get_first_last has the following parameter:

s (string): The input string.

Returns

string: A new string made of the first 2 and last 2 characters (e.g., "Python" becomes "Pyon").

If the string length is less than 2, it should return the string "Error: String is too short."

Sample Input 1

programming
Sample Output 1 (if you were to print the result)

prng
Sample Input 2

hi
Sample Output 2 (if you were to print the result)

hihi
Sample Input 3

a
Sample Output 3 (if you were to print the result)

Error: String is too short.'''

def get_first_last(s):
    first = ""
    second = ""
    get_first_last = ""
    if (len(s) >= 2):
        first = s[:2]
        second = s[-2:] 
        get_first_last = first+second
        return get_first_last
    else:
        return 'Error: String is too short.'
    
print(get_first_last("programming"))
print(get_first_last("in"))
print(get_first_last("a"))
