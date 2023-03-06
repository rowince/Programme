# Find a pair with the given sum in an array

# nums = [8, 7, 2, 5, 3, 1]
# target = 10
# output- (8, 2), (7, 3)
nums = [8, 7, 2, 5, 3, 1]
target = 10


def findpair(arr, target):
    temp = {}
    val = []
    for i in range(len(arr)):
        diff = target-arr[i]
        if diff not in temp:
            temp[arr[i]] = i
        else:
            j = temp[diff]
            val.append((j, i))
    return val

print(findpair(nums, target))

def findpair(nums, target):
    size = len(nums)
    for i in range(size-1):
        for j in range(i+1, size):
            if nums[i] + nums[j] == target:
                print(f'Sum of Pair is {nums[i], nums[j]} :{i, j}')


# findpair(nums, target)

# complexity: o(n*2)
