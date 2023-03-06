# Least Number of Unique Integers after K Removals
# Input: arr = [5, 5, 4], k = 1
# Output: 1
# Explanation: Remove the single 4, only 5 is left.
from collections import Counter

# lst = [5, 5, 4]
lst = [4, 3, 1, 1, 3, 3, 2]

def removeUnique(arr):
    temp = {}
    new = []
    for i in arr:
        if i not in temp:
            temp[i] = 1
        else:
            temp[i] = temp[i] + 1
    for i in temp.items():
        if v==1:
            new.append[k]
    print(len(new))
removeUnique(lst)
# def removeUnique(arr):
#     counting = 0
#     for i in arr:
#         k = arr.count(i)
#         if k == 1:
#             counting = counting + 1
#     print(counting)
# removeUnique(lst)
