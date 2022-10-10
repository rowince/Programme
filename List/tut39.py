# Write a python program that takes below inputs from user and generates a random password
# • Character length
# • Mandatory Number of upper case letters
# • Mandatory Number of digits
# • Mandatory Number of special symbols

import string
import random

print('Enter The Character length:', end=' ')
Character_length = int(input())
print('Enter The Mandatory Number of Upper Case Letters:')
upper_case_length = int(input())
print('Enter The Mandatory Number of digits:')
digits_length = int(input())
print('Enter The Mandatory Number of special symbols:')
special_length = int(input())


def password(Character_length, upper_case_length=0, digits_length=0, special_length=0):
    TotalNumber = upper_case_length+digits_length+special_length
    Total = Character_length - TotalNumber
    letter = string.ascii_uppercase
    digit = string.digits
    special = string.punctuation
    lower_letter = string.ascii_lowercase
    chars = ''.join(random.choice(letter)
                    for char in range(upper_case_length))
    digs = ''.join(random.choice(digit) for dig in range(digits_length))
    spls = ''.join(random.choice(special) for spl in range(special_length))
    final = chars+digs+spls
    words = ''.join(random.choice(lower_letter)
                    for i in range(Total))
    FinalWord = final+words
    PASSWORD = list(FinalWord)
    random.shuffle(PASSWORD)
    PASSWORD = ''.join(PASSWORD)
    return PASSWORD


print(password(Character_length, upper_case_length, digits_length, special_length))
