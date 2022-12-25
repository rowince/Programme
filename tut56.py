# How to search, insert, and delete in an unsorted array

# serach
# input = [12, 34, 10, 6, 40]
# key = 40
# input = [12, 34, 10, 6, 40]
# key = 6


# def search_element_unsorted(arr, key):
#     flag = False
#     for i in range(len(arr)):
#         if arr[i] == key:
#             flag = True
#     if flag == True:
#         print('Key Element is present in arr Indexth No is: ', i)
#     else:
#         print('Key Element is Not present in arr')


# search_element_unsorted(input, key)

# time complexity is O(n)

# insert element
# input = [12, 34, 10, 6, 40]
# key = 60
# output = [12, 34, 10, 6, 40, 60]

# input = [12, 34, 10, 6, 40]
# key = 60


# def insert_element_unsorted(arr, key):
#     arr.append(key)
#     print(arr)


# insert_element_unsorted(input, key)
# time complexity is O(1)

# Insert at any position
# input = [12, 34, 10, 6, 40]
# key = 60
# pos = 4
# output = [12, 34, 10, 60, 6, 40]

# input = [12, 34, 10, 6, 40]
# key = 60
# pos = 4


# def insert_element_unsorted_any(arr, key, pos):
#     arr.insert(pos-1, key)
#     print(arr)


# insert_element_unsorted_any(input, key, pos)
# time complexity is O(1)

# delete element
# input = [12, 34, 10, 6, 40]
# key = 6
# output = [12, 34, 10, 40]

input = [12, 34, 10, 6, 40]
key = 6


def delete_element_unsorted(arr, key):
    arr.remove(key)
    print(arr)


delete_element_unsorted(input, key)
# time complexity is O(1)
