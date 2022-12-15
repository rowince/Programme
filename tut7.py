# Check if element exists in list in Python

# list = [1, 6, 3, 5, 3, 4]
# Input: 3  # Check if 3 exist or not.
# Output: True

list = [1, 6, 3, 5, 3, 4]
target = 30

# for loop

# for i in list:
#     if i == target:
#         flag = 1
#         break
#     else:
#         flag = 0
# if flag:
#     print("True")
# else:
#     print("False")

# if_else

# if target in list:
#     print("True")
# else:
#     print("False")

#list_comprehension

# result = "True" if target in list else "False"
# print(result)

#lambada function

result = lambda x, target: "True" if target in x else "False"
print(result(list, target))