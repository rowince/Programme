# Python program to check if a string is palindrome or not
#palindrome- reverse the string is same as original string

x = '12321'

def palindrome(x):
    rev = ''
    for i in x:
        rev = i + rev
    if rev == x:
        print("Yes, This is a Palindrome")
    else:
        print("No, This is not a Palindrome")

palindrome(x)