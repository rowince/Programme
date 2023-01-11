# sort the list
# input = [20, 10, 20, 4, 100]
# output = [4, 10, 20, 20, 100]

list2 = [20, 10, 20, 4, 100]
# def sort_list(lis):
#     size = len(lis)
#     for i in range(size):
#         for j in range(i+1, size):
#             if lis[i] > lis[j]:
#                 temp = lis[i]
#                 lis[i] = lis[j]
#                 lis[j] = temp
#     return lis
# print(sort_list(list2))

new_list = []
while list2:
    mini = list2[0]
    for i in list2:
        if i < mini:
            mini = i
    new_list.append(mini)
    list2.remove(mini)
print(new_list)
