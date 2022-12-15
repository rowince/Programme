# Python program to check whether the string is Symmetrical or Palindrome
# symmetrical- A string is said to be symmetrical if both the halves of the string are the same
# palindrome-  a string is said to be a palindrome string if one half of the string is the reverse of the other half or if a string appears same when read forward or backward.

# Input: khokho
# Output: 
# The entered string is symmetrical
# The entered string is not palindrome

# Input:amaama
# Output:
# The entered string is symmetrical
# The entered string is palindrome

x = 'khokho'
y = 'amaama'
def palindrome(str):
    rev = ''
    for i in str:
        rev = i + rev
    if rev == str:
        print('The entered string is palindrome')
    else:
        print('The entered string is not palindrome')

# palindrome(y)

def symmetric(str):
    mid = len(str) // 2
    flag = 0
    for i in range(mid):
        if str[i] == str[mid+i]:
            flag = 1
        else:
            break
    if flag==1:
        print('The entered string is symmetrical')
    else:
        print('The entered string not is symmetrical')
symmetric(x)
        
    
    