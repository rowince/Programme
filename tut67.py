# x = ["a","!","b","@","c","#","d"]
# #out = ['d', '!', 'c', '@', '#', 'a']

x = ["a", "!", "b", "@", "c", "#", "d"]


def fun(x):
    temp = [i if i.isalpha() else None for i in x]
    temp = temp[::-1]
    for i in range(len(x)):
        if x[i].isalpha():
            x[i] = temp[i]
    print(x)


fun(x)
