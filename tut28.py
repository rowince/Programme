# Python | Program to print duplicates from a list of integers

# Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# Output : output_list = [20, 30, -20, 60]


from collections import Counter
list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

# time complexity O(n)


# def find_duplicates(arr):
#     temp = []
#     arr.sort()
#     for i in range(len(arr)-1):
#         j = i + 1
#         if arr[i] == arr[j] and arr[i] not in temp:
#             temp.append(arr[i])
#     print(temp)


# find_duplicates(list)

# time complexity O(n)


def find_duplicates(arr):
    temp = []
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j] and arr[i] not in temp:
                temp.append(arr[i])
    print(temp)


find_duplicates(list)


# l1 = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
# d = Counter(l1)
# print(d)
# print(d.keys())
# print(d.values())
# print(d.items())

# new_list = list([item for item in d if d[item] > 1])
# print(new_list)
# x = 'aabbbccade'
# y = []
# y.extend(x)
# print(y)
# y1 = Counter(y)
# print(y1)
# new_list = list([item for item in y1 if y1[item] == 1])
# print(new_list)

# x = 'aabbbcc'
# out= a2b3c2
# y = {}
# for i in x:
#     if i not in y:
#         y[i] = 1
#     else:
#         y[i] = y[i] + 1
# out = ''
# for k, v in y.items():
#     out = out + k + str(v)
# print(out)
# print(y)

#----------------------------------------------------------------------------------------------------#

#input = x = {'a':2, 'b':4, 'c':5}
#output = 'a2b4c5'

# x = {'a': 2, 'b': 4, 'c': 5}
# print(x)
# y = ''
# for k, v in x.items():
#     y = y+k
#     y = y+str(v)
# print(y)
