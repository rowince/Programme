# Python program to find largest number in a list

# Input : list2 = [20, 10, 20, 4, 100]
# Output : 100

import sys
list2 = [20, 10, 20, 4, 100]
# list2 = [20, 30]


def maxl(arr):
    mx = -sys.maxsize
    for i in arr:
        if i > mx:
            mx = i
    print(mx)


maxl(list2)


# class based


# class Pair:
#     def __init__(self):
#         self.max = 0


# def find_max(arr):
#     size = len(arr)
#     max_val = Pair()
#     if size == 1:
#         max_val.max = arr[0]
#         return max_val.max
#     if arr[0] > arr[1]:
#         max_val.max = arr[0]
#     else:
#         max_val.max = arr[1]
#     for i in range(2, size):
#         if arr[i] > max_val.max:
#             max_val.max = arr[i]
#     return max_val.max


# print(find_max(list2))

# function based

# def find_max(arr):
#     max_value = arr[0]
#     for i in arr:
#         if i > max_value:
#             max_value = i
#     return max_value
# print(find_max(list2))
# time complexity=O(n)

# max function

# x = max(list2)
# print(x)

# sort function

# list2.sort()
# print(list2[-1])

# for loop

# mx = list2[0]
# for i in range(1, len(list2)):
#     if list2[i] > mx:
#         mx = list2[i]
# print(mx)

# function


# def sort_list(lis):
#     size = len(lis)
#     for i in range(size):
#         for j in range(i+1, size):
#             if lis[i] > lis[j]:
#                 temp = lis[i]
#                 lis[i] = lis[j]
#                 lis[j] = temp
#     return lis


# print(sort_list(list2))
