# Python program to swap two elements in a list

# Input : [23, 65, 19, 90]
# pos1 = 1
# pos2 = 3
# Output : [19, 65, 23, 90]

x = [23, 65, 19, 90]
pos1 = 1
pos2 = 3

def swap_pos(list, pos1, pos2):
    temp = list[pos1]
    list[pos1] = list[pos2]
    list[pos2] = temp
    print(list)

swap_pos(x, pos1-1, pos2-1)

    
