# find the anagram group
# abc bca cab
# def edf
# list1 = ['abc', 'bca', 'cab', 'def', 'edf', 'fisnius']
# output = [['abc', 'bca', 'cab'], ['def', 'edf']]
from collections import Counter

list1 = ['abc', 'bca', 'cab', 'def', 'edf', 'fisnius']


def anagram_match(arr):
    new_anagram = {}
    for i in arr:
        new = str(sorted(i))
        if new in new_anagram:
            new_anagram[new].append(i)
        else:
            new_anagram[new] = [i]
    temp = [ana for ana in new_anagram.values() if len(ana) > 1]
    print(temp)


anagram_match(list1)

# def anagram_match(arr):
#     new_anagram = []
#     for i in list1:
#         new = sorted(i)
#         temp = []
#         for j in list1:
#             new_j = sorted(j)
#             if new == new_j:
#                 temp.append(j)
#         if temp not in new_anagram and len(temp)>1:
#             new_anagram.append(temp)
#     print(new_anagram)
# anagram_match(list1)
