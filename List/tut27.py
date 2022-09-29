# Python | Remove empty tuples from a list

# Input : tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'), 
#                   ('krishna', 'akbar', '45'), ('',''),()]
# Output : [('ram', '15', '8'), ('laxman', 'sita'), 
#           ('krishna', 'akbar', '45'), ('', '')]

list1 = [(), ('ram','15','8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), ('',''),()]
list2 = []

# for loop
# for i in list1:
#     if len(i) != 0:
#         list2.append(i)

for i in list1:
    if i != ():
        list2.append(i)
print(list2)

# list comprehension

# lis = [i for i in list1 if i]
# print(lis)

# filter method

# lis = list(filter(None, list1))
# print(lis)