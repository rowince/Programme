# Python program to interchange first and last elements in a list

# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# x = [12, 35, 9, 56, 24]

# def swap(list):
#     size = len(list)
#     temp = list[0]
#     list[0] = list[size - 1]
#     list[size - 1] = temp
#     print(list)

# swap(x)

x = [12, 35, 9, 56, 24]

def swap(list):
    size = len(list)
    list[0], list[size-1] = list[size-1], list[0]
    print(list)

swap(x)