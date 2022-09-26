# Python program to print odd numbers in a List

# Input: list2 = [12, 14, 95, 3, 73]
# Output: [95, 3, 73]

list2 = [12, 14, 95, 3, 73]

# for loop
# odd = []
# for i in list2:
#     if i % 2 !=0:
#         odd.append(i)
# print(odd)

# list comprehension

# odd = [i for i in list2 if i % 2 != 0]
# print(odd)

# filter function

odd = list(filter(lambda x: x % 2 != 0, list2))
print(odd)
