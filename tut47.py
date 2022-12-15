# remove i’th character from string in Python
# test_str = "GeeksForGeeks"
# Removing char at pos 3
# output: GeksForGeeks

test_str = "GeeksForGeeks"
pos = 3


# for loop
# new_str = ''
# for i in range(len(test_str)):
#     if i != pos-1:
#         new_str = new_str + test_str[i]

# print(new_str)

# built in replace mathod
new_str = test_str.replace(test_str[pos-1], '', 1)
print(new_str)
