# Python program to find the sum of a Sublist

# Input: arr = [2,4,5,10], i = 1, j = 3
# Output: 19

arr = [2,4,5,10]
i = 1
j = 3

# for loop
# ans = 0
# for item in range(i, j+1):
#     ans = ans + arr[item]
# print(ans)

# sum function

ans = sum(arr[i:j+1])
print(ans)