# Python | Count occurrences of an element in a list

# Input: lst = [15, 6, 7, 10, 12, 20, 10, 28, 10], x = 10
# Output: 3 
# Explanation: 10 appears three times in given list.

x = [15, 6, 7, 10, 12, 20, 10, 28, 10]
target = 10
count = 0

#for loop
# for i in x:
#     if i == target:
#         count = count + 1
# print(count)

#built in method
# y = x.count(10)
# print(y)

# using list_comprehension

count = [i for i in x if i == target]
print(len(count))
