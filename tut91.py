# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:
l1 = [2, 4, 3]
l2 = [5, 6, 4]


def sum_word(arr1, arr2):
    if len(arr1) > len(arr2):
        big = len(arr1)
        small = len(arr2)
        big_arr = arr1
        small_arr = arr2
    else:
        big = len(arr2)
        small = len(arr1)
        big_arr = arr2
        small_arr = arr1
    temp = [i for i in range(big)]
    carry = 0
    count = 0
    for i in range(big):
        if small > count:
            te = big_arr[i]+small_arr[i]+carry
            carry = 0
            if len(str(te)) > 1:
                te = str(te)
                temp[i] = int(te[-1])
                carry = int(te[:-1])
            else:
                temp[i] = te
            count = count+1
        else:
            te = big_arr[i]+carry
            carry = 0
            if len(str(te)) > 1:
                te = str(te)
                temp[i] = int(te[-1])
                carry = int(te[:-1])
            else:
                temp[i] = te

    print(temp)


sum_word(l1, l2)
