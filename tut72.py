# Print All Distinct Elements of a given integer array
# Input: arr[] = {12, 10, 9, 45, 2, 10, 10, 45}
# Output: 12, 10, 9, 45, 2

from collections import Counter
arr = [12, 10, 9, 45, 2, 10, 10, 45]


def distinctarr(arr):
    # temp = Counter(arr)
    # new = [i for i in temp]
    new = []
    [new.append(i) for i in Counter(arr)]
    print(new)


distinctarr(arr)


# def distinctarr(arr):
#     temp = []
#     for i in arr:
#         if i not in temp:
#             temp.append(i)
#     print(temp)
# distinctarr(arr)
