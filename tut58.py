import heapq
from heapq import heappop


# Function to find the k'th smallest element in a list using min-heap
# def find_kth_smallest(input, k):

#     # base case
#     if not input or len(input) < k:
#         exit(-1)

#     # transform the input list into a min-heap
#     heapq.heapify(input)

#     # pop from min-heap exactly `k-1` times
#     while k > 1:
#         heappop(input)
#         k = k - 1

#     # return the root of min-heap
#     return input[0]


# if __name__ == '__main__':

#     input = [7, 4, 6, 3, 9, 1]
#     k = 3

#     print('k\'th smallest element in the list is', find_kth_smallest(input, k))


def find_Kth_Largest(nums, k):
    """
    :type nums: List[int]
    :type of k: int
    :return value type: int
    """
    h = []
    for e in nums:
        heapq.heappush(h, (-e, e))
    for i in range(k):
        w, e = heapq.heappop(h)
        if i == k - 1:
            return e


input = [7, 4, 6, 3, 9, 1]
k = 3
print(find_Kth_Largest(input, k))
