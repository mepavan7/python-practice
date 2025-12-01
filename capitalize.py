
# Complete the solve function below.
def solve(s):
    is_start_of_word = True
    result = ""
    for i in range(len(s)):
        if s[i] == " ":
            result += " "
            is_start_of_word = True
        elif s[i] != "" and is_start_of_word is True:
            result += s[i].upper()
            is_start_of_word = False
        elif s[i] != "" and is_start_of_word is False:
            result += s[i].lower()
    return result
#s = input("Enter the name:")
print(solve(input("Enter the name:")))
            