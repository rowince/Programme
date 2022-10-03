# Python – Swap elements in String list

# list1 = ['Gfg', 'is', 'best', 'for', 'Geeks']
# ans =  ['efg', 'is', 'bGst', 'for', 'eGGks']
# e=G, G=e

list1 = ['Gfg', 'is', 'best', 'for', 'Geeks']
# for loop
# list2 = []
# for i in list1:
#     temp = ''
#     for j in i:
#         if j == 'G':
#             rep = j.replace('G', 'e')
#             temp += rep
#         elif j == 'e':
#             rep = j.replace('e', 'G')
#             temp += rep
#         else:
#             temp+=j
#     list2.append(temp)
# print(list2)

# list comprehension

list2 = [i.replace('G', '-').replace('e', 'G').replace('-', 'e') for i in list1]
print(list2)
