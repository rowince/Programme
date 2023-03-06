#

lst = [11, 12, 13, 14, 15]
output = [15, 13, 11, 12, 14]

def seriesNum(arr):
    mid = len(arr)//2
    temp = [i for i in range(len(arr))]
    temp[mid] = arr[0]
    arr.remove(arr[0])
    low = high = mid
    while arr:
        temp[high+1] = arr[0]
        arr.remove(arr[0])
        temp[low-1] = arr[0]
        arr.remove(arr[0])
        high = high + 1
        low = low - 1
    temp = " ".join([str(i) for i in temp])
    print(temp)
    
seriesNum(lst)

