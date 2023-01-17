# Reorder an array according to given indexes
# Input:  arr[]   = [10, 11, 12];
#             index[] = [1, 0, 2];
# Output: arr[]   = [11, 10, 12]
#            index[] = [0,  1,  2]

arr = [10, 11, 12]
index = [1, 0, 2]


def arrindex(arr, index):
    temp_dict = sorted(zip(index, arr))
    temp = []
    for i in temp_dict:
        temp.append(i[1])
    print(temp)


arrindex(arr, index)
