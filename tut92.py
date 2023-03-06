# find the keprekars numbers
# keprakres number is -- 45*45=2025, 20+25=45
import math
lst = 10000


def kepreakers(arr):
    for i in range(1, arr):
        if i == 1:
            print(i, end=' ')
        else:
            number = i*i
            count = 1
            while not number == 0:
                count = count + 1
                number = number // 10
            number = i*i
            j = 0
            while j < count:
                j = j + 1
                split = int(math.pow(10, j))
                if split == i:
                    continue
                total = number//split + number % split
                if total == i:
                    print(i, end=' ')


kepreakers(lst)


# def kepreakers(arr):
#     for i in range(1, arr):
#         number = i*i
#         num = str(number)
#         if len(num) < 2:
#             num = '0'+num
#         mid = len(num)//2
#         first_half = int(num[:mid])
#         second_half = int(num[mid:])
#         if first_half+second_half == i:
#             print(i, end=' ')


# kepreakers(lst)
