# Product of Array except itself

# input = [2, 3, 4, 5]
# output = [60, 40, 30, 24]

x = [2, 3, 4, 0]


def productexcept(list):
    prod = 1
    temp = 0
    for i in range(len(list)):
        if list[i] == 0:
            temp = temp + 1
        else:
            prod = prod * list[i]
    arr = [i for i in range(len(list))]
    for i in range(len(list)):
        # temp == 0 and list[i] != 0
        if temp == 0:
            arr[i] = prod // list[i]
        # temp == 1 and list[i] != 0
        elif temp == 1 and list[i] != 0:
            arr[i] = 0
        # temp == 1 and list[i] == 0
        elif temp > 1:
            arr[i] = 0
        # temp == 1 and list[i] == 0
        else:
            arr[i] = prod
    print(arr)


productexcept(x)
