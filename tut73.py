# Rearrange an array such that arr[i] = i
# Given an array of elements of length N, ranging from 0 to N – 1. All elements may not be present in the array. If the element is not present then there will be -1 present in the array. Rearrange the array such that A[i] = i and if i is not present, display -1 at that place.

# Input : arr = {-1, -1, 6, 1, 9, 3, 2, -1, 4, -1}
# Output : [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]

arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]


def rearrange(arr):
    size = len(arr)
    temp = []
    for i in range(size):
        temp.append(arr[i])
    for i in range(size):
        if i in temp:
            arr[i] = i
        else:
            arr[i] = -1
    print(arr)


rearrange(arr)
