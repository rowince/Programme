# write a programme for factorial

# using for loop
# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         fact = 1
#         for i in range(2, n+1):
#             fact = fact * i
#         return fact

# print(factorial(4))


# using recursion

def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)


print(factorial(4))
