# Python program to find smallest number in a list

# Input : list1 = [10, 20, 4]
# Output : 4

list1 = [10, 20, 4, 30, 22, 2, 45]
# list1 = [1, 3]

# class based
# import sys

# def smal(arr):
#     sm = sys.maxsize
#     for i in arr:
#         if i < sm:
#             sm = i
#     print(sm)
# smal(list1)

# class Pair:
#     def __init__(self):
#         self.min = 0


# def find_min(arr):
#     size = len(arr)
#     min_pair = Pair()
#     if size == 1:
#         min_pair.min = arr[0]
#         return min_pair.min
#     if arr[0] > arr[1]:
#         min_pair.min = arr[1]
#     else:
#         min_pair.min = arr[0]
#     for i in range(2, size):
#         if arr[i] < min_pair.min:
#             min_pair.min = arr[i]
#     return min_pair.min


# print(find_min(list1))


# # function


# def find_min(arr):
#     min_value = arr[0]
#     for i in arr:
#         if i < arr[0]:
#             min_value = i
#     print(min_value)


# find_min(list1)

# time complexity O(n)

# for loop
# min = list1[0]
# for i in list1:
#     if i < min:
#         min = i
# print(min)

# sort method

# list1.sort()
# print(list1[0])

# min function

# x = min(list1)
# print(x)
