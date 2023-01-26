# Python | Program to remove duplicates/unique from a list of integers

# Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# Output : output_list = [10, 20, 30, 40, 50, -20, 60]

from collections import Counter
arr = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

# # approach 1


# def unique(arr):
#     temp = []
#     for i in arr:
#         c = arr.count(i)
#         if c == 1:
#             temp.append(i)
#     print(temp)
# unique(arr)

# def remove_duplicate(arr):
#     temp = []
#     for i in arr:
#         if i not in temp:
#             temp.append(i)
#     print(temp)


# remove_duplicate(arr)

# approach 2


# def remove_duplicate(arr):
#     counter = Counter(arr)
#     arr = [i for i in counter]
#     print(arr)


# remove_duplicate(arr)

# approach 3

# new = [j for i, j in enumerate(arr) if j not in arr[:i]]
# print(new)
# from math import prod
# new = []
# [new.append(i) for i in arr if i not in new]
# print(new)
# print(prod(new))