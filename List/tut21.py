# Python program to print all even numbers in a range

# Input: start = 4, end = 15
# Output: 4, 6, 8, 10, 12, 14

# start = 4
# end = 15

# built in step method
# for num in range(start, end, 2):
#     print(num, end=" ")

# for loop
# even = []
# for i in range(start, end+1):
#     if i%2 == 0:
#         even.append(str(i))
# eve = ', '.join(even)
# print(eve)

# list comprehension
# even = [str(i) for i in range(start, end+1) if i%2==0]
# print(','.join(even))

# filter method
# eve = [i for i in range(start, end+1)]

# even = list(filter(lambda x: x%2==0, eve))
# print(even)

print("Enter The Start Number: ")
start = int(input())
print("Enter The End Number: ")
end = int(input())
for i in range(start, end+1):
    if i % 2 == 0:
        print(i, end=' ')
