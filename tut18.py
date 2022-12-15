# Python program to print even numbers in a list

# Input: list1 = [2, 7, 5, 64, 14]
# Output: [2, 64, 14]

list1 = [2, 7, 5, 64, 14]

#for loop
# even = []
# for i in list1:
#     if i%2 == 0:
#         even.append(i)
# print(even)

#list comprehension
# even = [i for i in list1 if i%2==0]
# print(even)

# filter function

# even = list(filter(lambda x: x%2 ==0, list1))
# print(even)

# lambada function

even = lambda x: x%2 == 0
print(even(3))