# Find the largest three distinct elements in an array
# Input: arr = [10, 4, 3, 50, 23, 90]
# Output: 90, 50, 23

import sys

arr = [10, 4, 3, 50, 23, 90, 90]


def largest3(arr):
    arr.sort()
    size = len(arr)
    check = 0
    count = 1
    for i in range(1, size+1):
        if count < 4:
            if check != arr[size-i]:
                print(arr[size-i], end=' ')
                check = arr[size-i]
                count = count + 1
        else:
            break


largest3(arr)


# def largest3(arr):
#     size = len(arr)
#     if size < 3:
#         print('Invalid Input')
#         return
#     first = second = third = -sys.maxsize
#     for i in range(size):
#         if arr[i] > first:
#             third = second
#             second = first
#             first = arr[i]
#         elif arr[i] > second:
#             third = second
#             second = arr[i]
#         elif arr[i] > third:
#             third = arr[i]
#     print(
#         f"The Three Largest Item is First: {first} Second: {second} Third: {third}")


# largest3(arr)
# Time Complexity: O(n)
