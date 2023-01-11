# Alternative Sorting
# # Given an array of integers, print the array in such a way that the first element is first maximum and second element is first minimum and so on.
# Input : arr[] = [7, 1, 2, 3, 4, 5, 6]
# Output : 7 1 6 2 5 3 4

arr = [7, 1, 2, 3, 4, 5, 6]


def alternate_max_min_sort(arr):
    temp = []
    arr.sort()
    while arr:
        if len(arr) == 1:
            temp.append(arr[0])
            arr.remove(arr[0])
        else:
            mx = arr[-1]
            mn = arr[0]
            temp.append(mx)
            temp.append(mn)
            arr.remove(mx)
            arr.remove(mn)
    temp = ' '.join([str(i) for i in temp])
    print(temp)


alternate_max_min_sort(arr)
