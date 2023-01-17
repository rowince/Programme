# Program for array left rotation by d positions.
# Given an array of integers arr[] of size N and an integer, the task is to rotate the array elements to the left by d positions.
# Input:
# arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
# Output: 3 4 5 6 7 1 2

arr = [1, 2, 3, 4, 5, 6, 7]
d = 2


def rotate(arr, d):
    temp = []
    for i in range(d):
        temp.append(arr[i])
    for i in arr[:]:
        if i in temp:
            arr.remove(i)
    arr.extend(temp)
    print(arr)


rotate(arr, d)
