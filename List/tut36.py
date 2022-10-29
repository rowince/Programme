# Python program to check if a string is palindrome or not
# palindrome- reverse the string is same as original string

import re


x = '12321'

# def palindrome(x):
#     rev = ''
#     for i in x:
#         rev = i + rev
#     if rev == x:
#         print("Yes, This is a Palindrome")
#     else:
#         print("No, This is not a Palindrome")

# palindrome(x)

# using recursion


def palindrome(str):
    str = str.lower()
    size = len(str)
    if size < 2:
        return True
    elif str[0] == str[size-1]:
        return palindrome(str[1:size-1])
    else:
        return False


res = palindrome(x)
if res:
    print('Palindrome')
else:
    print('Not Palindrome')
