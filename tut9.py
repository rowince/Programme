# Reversing a List in Python

# Input : [4, 5, 6, 7, 8, 9]
# Output : [9, 8, 7, 6, 5, 4]

x = [4, 5, 6, 7, 8, 9, 1]


def rev(arr):
    size = len(arr)
    start = 0
    end = size - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start = start + 1
        end = end - 1
    print(arr)


rev(x)


# for loop
# reverse = []
# for i in x:
#     reverse.insert(0, i)
# print(reverse)

# reverse method

# x.reverse()
# print(x)

# slice method

# reverse = x[::-1]
# print(reverse)

# list comprehension method

# reverse = [x[len(x)-i] for i in range(1, len(x)+1)]
# print(reverse)
