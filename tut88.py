# ([2,4,9,6,3,8,5,7] , 22)

# [4,9,6,,3] = 4 + 9 + 6 + 3 == 22
# [4,9,6,3]
# -1

arr = [2, 4, 9, 6, 3, 8, 5, 7]
target = 12

def seq_num(arr, num):
    while arr:
        sum = 0
        temp = []
        for j in range(len(arr)):
            if sum != num:
                sum = sum+arr[j]
                temp.append(arr[j])
                if sum > num:
                    break
        if sum == num:
            return temp
        arr.pop(0)
    return -1


print(seq_num(arr, target))
