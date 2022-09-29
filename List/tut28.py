# Python | Program to print duplicates from a list of integers

# Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# Output : output_list = [20, 30, -20, 60]

from multiprocessing.reduction import duplicate


list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

# for loop
# output_list = []
# for i in range(len(list)):
#     k = i+1
#     for j in range(k, len(list)):
#         if list[i] == list[j] and list[i] not in output_list:
#             output_list.append(list[i])
# print(output_list)