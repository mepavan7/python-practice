s = ['a', 'b', 'b', 'a', 'c', 'a']
#res = s[len(s)-1]
L = len(s)
result = []
for i in range(L):
   if result and result[-1] == s[i]:
        result.pop()
   else:
        result.append(s[i])
print(result)

'''
Methods to check if a list is empty
1. Use len() to check the length 
Concept: The len() function returns the number of items in a list. If the list is empty, its length will be 0.

my_list = []
if len(my_list) == 0:
    print("The list is empty")
else:
    print("The list is not empty")

2. Use truthiness evaluation 
Concept: In Python, empty sequences like lists, strings, and tuples are considered "falsey," meaning they evaluate to False in a boolean context. Non-empty sequences are "truthy".

my_list = []
if not my_list:
    print("The list is empty")
else:
    print("The list is not empty")

Why it's preferred: This is often considered the most "Pythonic" or cleanest way to check for an empty list. 

3. Compare to an empty list literal
Concept: You can directly compare the list to an empty list ([]).
my_list = []
if my_list == []:
    print("The list is empty")
else:
    print("The list is not empty")


[1] https://www.geeksforgeeks.org/python/python-check-if-list-empty-not/
[2] https://www.pythonmorsels.com/checking-for-an-empty-list-in-python/
[3] https://www.quora.com/How-do-I-check-if-a-list-is-empty-in-Python
[4] https://www.freecodecamp.org/news/how-to-check-if-a-list-is-empty-in-python/
[5] https://www.askpython.com/python/list/check-if-list-is-empty
[6] https://www.youtube.com/watch?v=VS9km2_ALIM
[7] https://stackoverflow.com/questions/53513/how-do-i-check-if-a-list-is-empty

'''