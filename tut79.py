# Sort Python Dictionaries by Key or Value

# sort the dict by key
# Input:
# {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}

# Output:
# {'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash': 2}
from operator import itemgetter

x = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}


# def dict_sort(arr):
#     sort_dict = dict(sorted(arr.items()))
#     print(sort_dict)


# dict_sort(x)


def dict_sort(arr):
    sort_dict = dict(sorted(arr.items(), key=itemgetter(1)))
    print(sort_dict)


dict_sort(x)

# sort the dict by value
# Input:
# {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}

# Output:
# {'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash': 2}

x = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}


# def dict_val(arr):
#     arr = list(arr.items())
#     for i in range(len(arr)-1):
#         for j in range(i+1, len(arr)):
#             if arr[i][1] > arr[j][1]:
#                 arr[i], arr[j] = arr[j], arr[i]
#     arr = dict(arr)
#     print(arr)


# dict_val(x)

# def dict_val(arr):
#     sort_dict = dict(sorted(arr.items(), key=itemgetter(1)))
#     print(sort_dict)


# dict_val(x)
