# Python program to print all odd numbers in a range

# Input: start = 4, end = 15
# Output: 5, 7, 9, 11, 13, 15

start = 4
end = 15

# built in step method
# for i in range(start, end+1):
#     if i%2 != 0:
#         print(i, end=' ')
  
# list comprehension

# odd = [i for i in range(start, end+1) if i%2 != 0]      
# print(odd)

# fillter

od = [i for i in range(start, end+1)]
odd = list(filter(lambda x: x%2 != 0, od))
print(odd)
