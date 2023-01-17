# Extract elements with Frequency greater than K
# Input : test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
# Output : [4, 3]

test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
K = 3

# approach 1

# def count_frequency(arr, k):
#     temp_dict = {}
#     for i in arr:
#         if i not in temp_dict:
#             temp_dict[i] = 1
#         else:
#             temp_dict[i] = temp_dict[i] + 1
#     temp = []
#     for i, j in temp_dict.items():
#         if j >= k:
#             temp.append(i)
#     print(temp)


# count_frequency(test_list, K)


# approach 2

def count_frequency(arr, k):
    temp = []
    for i in arr:
        f = arr.count(i)
        if f >= k and i not in temp:
            temp.append(i)
    print(temp)


count_frequency(test_list, K)
