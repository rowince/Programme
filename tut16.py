# Python program to find second largest number in a list

# Input: list2 = [70, 11, 20, 4, 100]
# Output: 70

import sys
list2 = [100, 90, 11, 20, 4, 70]


def secmx(arr):
    first = second = -sys.maxsize
    for i in arr:
        if i > first:
            second = first
            first = i
        elif i > second:
            second = i

    print(second)


secmx(list2)


# sort method
# list2.sort()
# print(list2[-2])

# for loop

# mx = max(list2[0], list2[1])
# secmx = min(list2[0], list2[1])
# for i in range(2, len(list2)):
#     if list2[i] > mx:
#         secmx = mx
#         mx = list2[i]
#     elif list2[i] > secmx and mx != list2[i]:
#         secmx = list2[i]
#     elif mx == secmx and secmx != list2[i]:
#         secmx = list2[i]
# print(secmx)
