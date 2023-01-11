# Sort an array according to absolute difference
# Input: val = 6, a = [7, 12, 2, 4, 8, 0]
# Output: a = [7 4 8 2 12 0]
# Explanation: Consider the absolute difference of each array element and ‘val’ 7 – 6 = 1 12- 6 = 6 2 – 6 = 4 (abs) 4 – 6 = 2 (abs) 8 – 6 = 2 0 – 6 = 6 (abs) So, according to the obtained differences, sort the array differences in increasing order, 1, 2, 2, 4, 6, 6 is obtained, and their corresponding array elements are 7, 4, 8, 2, 12, 0.

from operator import itemgetter

arr = [7, 12, 2, 4, 8, 0, 7]
target = 6


def abolute_sort(arr, target):
    temp = []
    for i in arr:
        temp_arr = []
        diff = abs(i - target)
        temp_arr.append(i)
        temp_arr.append(diff)
        temp.append(temp_arr)
    sorted_temp = sorted(temp, key=itemgetter(1))
    temp_list = [i[0] for i in sorted_temp]
    print(temp_list)


abolute_sort(arr, target)

# def abolute_sort(arr, target):
#     temp = {}
#     for i in arr:
#         diff = abs(i - target)
#         temp[i] = diff
#     sorted_temp = dict(sorted(temp.items(), key=itemgetter(1)))
#     temp_list = [i for i in sorted_temp]
#     print(temp_list)


# abolute_sort(arr, target)


# def printsorted(a, n, val):

#     # declare a 2-D matrix
#     b = [[0 for x in range(2)] for y in range(n)]

#     for i in range(0, n):
#         b[i][0] = abs(a[i]-val)
#         b[i][1] = i

#     b.sort()

#     for i in range(0, n):
#         print(a[b[i][1]])


# n = len(arr)
# val = 6
# printsorted(arr, n, val)
