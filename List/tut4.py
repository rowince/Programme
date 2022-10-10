# Maximum of two numbers in Python

# Input: a = 2, b = 4
# Output: 4

a = 2
b = 4

# built-in method
# start = time.time()
# maximum = max(a, b)
# end = time.time()
# print("Maximum:", maximum)
# print("Time_Taken:", end-start)

# if else

# if a > b:
#     print("Maximum:", a)
# else:
#     print("Maximum:", b)

# lambada function

# maximum = lambda x, y: x if x > y else y
# print("Maximum:", maximum(a, b))

# list comprehension

maximum = a if a > b else b
print("Maximum:", maximum)
