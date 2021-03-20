spam = ['apples', 'bananas', 'tofu', 'cats']

"""
Write a function that takes a list value as an argument and returns a string with all 
the items separated by a comma and a space, with and inserted before the last item. For example, 
passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. 
But your function should be able to work with any list value passed to it.
"""

def my_func(my_lst):
    lst = ""
    l = len(my_lst)

    for idx, item in enumerate(my_lst):
        if idx + 1 != l:
            lst += f"{item}, " 
        else:
            lst += f" and {item}"
    print(lst)

my_func(spam)





