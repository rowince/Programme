# Rearrange array such that even positioned are greater than odd
# Input : A[] = {1, 2, 2, 1}
# Output :  1 2 1 2

# arr = [1, 2, 2, 1]
arr = [1, 3, 2, 2, 5]


def posevenodd(arr):
    for i in range(1, len(arr)):
        if (i % 2 == 0):
            if arr[i] > arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        else:
            if arr[i] < arr[i - 1]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
    print(arr)


posevenodd(arr)
