# decorator function

def greeting_extend(fun):
    def inner():
        print('Hello,')
        fun()
        print('Have a nice day')
    return inner


@greeting_extend
def greeting_morning():
    print('Good Morning')


print(greeting_morning())
# greeting_morning()
# my_fun = greeting_extend(greeting_morning)
# my_fun()


def division_not_fraction(fun):
    def inner(a, b):
        if a < b:
            d = b/a
            print('Division: ', d)
        else:
            fun(a, b)
    return inner


@division_not_fraction
def division(a, b):
    d = a/b
    print('Division: ', d)


# division(10, 2)
division(4, 10)
