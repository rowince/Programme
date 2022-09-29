# Remove common elements from two list in Python

# Input : list1 = [1, 2, 3, 4, 5]  
#         list2 = [4, 5, 6, 7, 8,]
# Output : list1 :  [1, 2, 3]
#         list2 :  [6, 7, 8]

list1 = [1, 2, 3, 4, 5]  
list2 = [4, 5, 6, 7, 8]

# for loop

# for i in list1[:]:
#     if i in list2:
#         list1.remove(i)
#         list2.remove(i)
# print(list1)
# print(list2)

# list comprehension

# lis1_1 = [i for i in list1 if i not in list2]
# lis1_2 = [i for i in list2 if i not in list1]
# print(lis1_1)
# print(lis1_2)

# set

list1_1 = list(set(list1).difference(set(list2)))
list1_2 = list(set(list2).difference(set(list1)))
print(list1_1)
print(list1_2)