# Two elements whose sum is closest to zero
# arr = [1, 60, -10, 70, -80, 85]
# -80 and 85

arr = [1, 60, -10, 70, -80, 85]


def closest_sum(arr):
    size = len(arr)
    first = None
    last = None
    min_sum = arr[0] + arr[1]
    for i in range(size-1):
        for j in range(i+1, size):
            if abs(arr[i] + arr[j]) < min_sum:
                min_sum = abs(arr[i] + arr[j])
                first = i
                last = j
    print("The two Elements are closest to item is %d, %d" %
          (arr[first], arr[last]))


closest_sum(arr)
