# Python – Avoid Spaces in string length
# Input : test_str = ‘geeksforgeeks 33 best’
# Output : 19

x = 'gee ksforgeeks 33 best'
# c = 0
# for i in x:
#     if i != ' ':
#         c = c+1
# print(c)
new_x = ''
for i in x:
    if i == ' ':
        new_x = new_x + ''
    else:
        new_x = new_x + i
print(len(new_x))
