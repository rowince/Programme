# An array contains both positive and negative numbers in random order. Rearrange the array elements so that positive and negative numbers are placed alternatively. A number of positive and negative numbers need not be equal. If there are more positive numbers they appear at the end of the array. If there are more negative numbers, they too appear at the end of the array.

# arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
# output = [9, -7, 8, -3, 5, -1, 2, 4, 6]

arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
# arr = [-1, 2, -3, 4, -5, -6, -7, 8, -9]


def arrangeposnegalternate(arr):
    neg = [i for i in arr if i < 0]
    pos = [i for i in arr if i > 0]
    for i in range(len(arr)):
        if len(pos) != 0 and len(neg) != 0:
            if i % 2 == 0:
                arr[i] = pos[0]
                pos.pop(0)
            else:
                arr[i] = neg[0]
                neg.pop(0)
        else:
            if len(pos) != 0:
                arr[i] = pos[0]
                pos.pop(0)
            else:
                arr[i] = neg[0]
                neg.pop(0)
    print(arr)

    # if len(pos) != 0:


    # size = abs(len(pos)-len(neg))
    # if len(pos) < len(neg):
    #     for i in range(size):
    #         arr[]
arrangeposnegalternate(arr)
