# fibonacii series
# num = 13
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

num = 13


def fibonacci(num):
    a = 0
    b = 1
    count = 0
    if num <= 0:
        print("Enter Only Positive Number.")
    elif num == 1:
        print(num)
    else:
        while count < num:
            print(a, end=' ')
            c = a + b
            a = b
            b = c
            count = count + 1


fibonacci(num)
