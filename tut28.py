# Python | Program to print duplicates from a list of integers

# Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# Output : output_list = [20, 30, -20, 60]


from collections import Counter
# list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

# for loop
# output_list = []
# for i in range(len(list)):
#     k = i+1
#     for j in range(k, len(list)):
#         if list[i] == list[j] and list[i] not in output_list:
#             output_list.append(list[i])
# print(output_list)


# l1 = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
# d = Counter(l1)
# print(d[2])

# new_list = list([item for item in d if d[item] > 1])
# print(new_list)
x = 'aabbbccad'
y = []
y.extend(x)
print(y)
y1 = Counter(y)
print(dict(y1))
# new_list = list([item for item in y1 if y1[item] == 1])
# print(new_list)

# x = 'aabbbcc'
# # out= a2b3c2
# y = {}
# for i in x:
#     if i not in y:
#         y[i] = 1
#     else:
#         y[i] = y[i] + 1
# print(y)
