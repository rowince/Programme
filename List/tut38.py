# Write a python program that takes a string as input and prints whether this string is a true palindrome or not. A true
# palindrome is a string such that if you remove all characters except for letters (uppercase and lowercase), the string is
# equal if read from left to right and from right to left. If the inputted string is a true palindrome, the message YES
# (uppercase required) is displayed else NO is displayed.
# Notice that lowercase letters are equal to uppercase letters and vice-versa.

def palindrome(input_string):
    word = ''.join([i.lower() for i in input_string if i.isalpha()])
    reverse = ''
    for i in word:
        reverse = i + reverse
    if reverse == word:
        return 'YES'
    else:
        return 'NO'

# print(palindrome('abut-1-tuba'))
