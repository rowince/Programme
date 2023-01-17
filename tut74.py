# Rearrange positive and negative numbers
# Input:  [12 11 -13 -5 6 -7 5 -3 -6]
# Output: [-13 -5 -7 -3 -6 12 11 6 5]

arr = [12, 11, -13, -5, 6, -7, 5, -3, -6]


def negpos(arr):
    pos = []
    neg = []
    for i in arr:
        if i < 0:
            neg.append(i)
        else:
            pos.append(i)
    # neg.extend(pos)
    print(neg)


negpos(arr)
