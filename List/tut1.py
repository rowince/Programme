# Python program to interchange first and last elements in a list

# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

from subprocess import list2cmdline


x = [12, 35, 9, 56, 24]

def swap(list):
    size = len(list)
    temp = list[0]
    list[0] = list[size - 1]
    list[size - 1] = temp
    print(list)

swap(x)