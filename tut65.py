# Sort elements by frequency
# Print the elements of an array in the decreasing frequency if 2 numbers have the same frequency then print the one which came first
# Input:  arr[] = {2, 5, 2, 8, 5, 6, 8, 8}
# Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6}
from collections import Counter
from operator import itemgetter
arr = [5, 2, 2, 8, 5, 6, 8, 8]


def sort_frequency(arr):
    temp_list = []
    arr.sort()
    temp = Counter(arr)
    sorted_temp = dict(sorted(temp.items(), key=itemgetter(1), reverse=True))
    print(sorted_temp)
    for k, v in sorted_temp.items():
        new = [k for i in range(v)]
        temp_list.extend(new)
    print(temp_list)


sort_frequency(arr)
