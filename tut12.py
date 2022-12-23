# Python | Sum of number digits in List

# input: [12, 67, 98, 34]
# output: [3, 13, 17, 7]

x = [12, 67, 98, 34]
# for loop
# count = []
# for i in x:
#     sum = 0
#     for j in str(i):
#         sum = sum + int(j)
#     count.append(sum)
# print(count)

# using map function

# count = list(map(lambda sub: sum(int(i) for i in str(sub)), x))
# print(count)
