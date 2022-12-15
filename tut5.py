# Minimum of two numbers in Python

a = 4
b = 2

# built-in function

# minimum = min(a, b)
# print("Minimum:", minimum)

# if else 

# if a < b:
#     print("Minimum:", a)
# else:
#     print("Minimum:", b)

#lambada function

# minimum = lambda x, y: x if x < y else y
# print("Minimum:", minimum(a, b))

# list comprehension

minimum = a if a < b else b
print("Minimum:", minimum)