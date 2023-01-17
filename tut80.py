# Merging two Dictionaries

# dict1 = {'a': 10, 'b': 8}
# dict2 = {'d': 6, 'c': 4}
# dict3 = {'a': 10, 'b': 8, 'd': 6, 'c': 4}


dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}


# def merge_dict(dict1, dict2):
#     dict1.update(dict2)
#     print(dict1)


# merge_dict(dict1, dict2)

# def merge_dict(dict1, dict2):
#     for i in dict2.keys():
#         dict1[i] = dict2[i]
#     print(dict1)


# merge_dict(dict1, dict2)

def merge_dict(dict1, dict2):
    dict3 = dict1 | dict2
    print(dict3)


merge_dict(dict1, dict2)
