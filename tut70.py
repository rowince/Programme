# Move all zeroes to end of array
# Input  [1, 2, 0, 0, 0, 3, 6]
# Output [1, 2, 3, 6, 0, 0, 0]

arr = [1, 2, 0, 0, 0, 3, 6]


# def movezero(arr):
#     temp = [i for i in arr if i != 0]
#     new = [i for i in arr if i == 0]
#     temp.extend(new)
#     print(temp)


# movezero(arr)

# def movezero(arr):
#     temp = []
#     count = 0
#     for i in range(len(arr)):
#         if arr[i] == 0:
#             arr[i] = None
#             count = count + 1
#     arr = [i for i in arr if i != None]
#     for i in range(count):
#         arr.append(0)
#     print(arr)


# movezero(arr)
