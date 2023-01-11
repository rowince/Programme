# Maximum and minimum of an array using minimum number of comparisons
# Input: arr[] = [3, 5, 4, 1, 9]
# Output: Minimum element is: 1
#         Maximum element is: 9

list2 = [3, 5, 4, 1, 9]
# list2 = [3, 10]


class Pair:
    def __init__(self, arr):
        self.min = 0
        self.max = 0
        self.arr = arr

    def find_maxmin(self):
        size = len(self.arr)
        if size == 1:
            self.min = self.arr[0]
            self.max = self.arr[0]
            return ("Minimum = %d, Maximum = %d" % (self.min, self.max))
        if self.arr[0] > self.arr[1]:
            self.min = self.arr[1]
            self.max = self.arr[0]
        else:
            self.min = self.arr[0]
            self.max = self.arr[1]
        for i in range(2, size):
            if self.arr[i] < self.min:
                self.min = self.arr[i]
            if self.arr[i] > self.max:
                self.max = self.arr[i]
        return ("Minimum = %d, Maximum = %d" % (self.min, self.max))


minmax = Pair(list2)
print(minmax.find_maxmin())
# class Pair:
#     def __init__(self):
#         self.min = 0
#         self.max = 0


# def find_maxmin(arr):
#     size = len(arr)
#     maxmin = Pair()
#     if size == 1:
#         maxmin.min = arr[0]
#         maxmin.max = arr[0]
#         return ("Minimum = %d, Maximum = %d" % (maxmin.min, maxmin.max))
#     if arr[0] > arr[1]:
#         maxmin.min = arr[1]
#         maxmin.max = arr[0]
#     else:
#         maxmin.min = arr[0]
#         maxmin.max = arr[1]
#     for i in range(2, size):
#         if arr[i] < maxmin.min:
#             maxmin.min = arr[i]
#         if arr[i] > maxmin.max:
#             maxmin.max = arr[i]
#     return ("Minimum = %d, Maximum = %d" % (maxmin.min, maxmin.max))


# print(find_maxmin(list2))


# function


# def find_maxmin(arr):
#     size = len(arr)
#     min_val = arr[0]
#     max_val = arr[0]
#     for i in range(1, size):
#         if arr[i] < min_val:
#             min_val = arr[i]
#         if arr[i] > max_val:
#             max_val = arr[i]
#     return ("Minimum = %d, Maximum = %d" % (min_val, max_val))


# print(find_maxmin(list2))
