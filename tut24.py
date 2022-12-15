# Python program to print negative numbers in a list

# Input: list1 = [12, -7, 5, 64, -14]
# Output: -7, -14

list1 = [12, -7, 5, 64, -14]

# for loop
# for i in list1:
#     if i < 0:
#         print(i, end=' ')

# list comprehension

# lis = [i for i in list1 if i < 0]
# print(lis)

# filter method

lis = list(filter(lambda x: x<0, list1))    
print(lis)