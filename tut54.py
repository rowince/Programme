import string
# sort string
# input_data = '2name 1my 4rowince 3is'
# output = 'my name is rowince'

input_data = '2name 1my 4rowince 3is'

# for function


def name(name_str):
    x = name_str.split()
    x.sort()
    temp = []
    for i in x:
        new = ''.join([j for j in i if j.isalpha()])
        temp.append(new)
    new = ' '.join(temp)
    print(new)


name(input_data)

# def name(name_str):
#     x = name_str.split()
#     x.sort()
#     temp = []
#     for i in x:
#         temp.append(i.translate(str.maketrans('', '', string.digits)))
#     new = ' '.join(temp)
#     print(new)


# name(input_data)

# for loop
# x = input_data.split()
# x.sort()
# temp = []
# for i in x:
#     temp_new = []
#     temp_new.extend(i)
#     str_j = ''
#     for j in temp_new:
#         if j.isalpha():
#             str_j = str_j + j
#     temp.append(str_j)
# y = ' '.join(temp)
# print(y)

# remove integer from list
# x = '1my'

# new = str.maketrans('', '', string.digits)
# new_str = x.translate(new)
# new_str = x.translate(str.maketrans('', '', string.digits))
# print(new_str)
