# Python | Reverse All Strings in String List

# The original list is : ['geeks', 'for', 'geeks', 'is', 'best']
# The reversed string list is : ['skeeg', 'rof', 'skeeg', 'si', 'tseb']

list1 = ['geeks', 'for', 'geeks', 'is', 'best']

# for loop
# list2 = []
# for i in list1:
#     rev = ''
#     for j in i:
#         rev = j + rev
#     list2.append(rev)
# print(list2)

# list comprehension

list2 = [i[::-1] for i in list1]
print(list2)
