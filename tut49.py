# python program to find the larget word in the strings avoid special char
# input = "funn&!! time"


def largestword(str):
    word = str.split()
    print(word)
    largest = ''
    for i in word:
        if i.isalpha() or i.isnumeric():
            if len(i) > len(largest):
                largest = i
            elif len(i) == len(largest):
                largest = largest
        else:
            temp = []
            temp.extend(i)
            lst = ''.join([j for j in temp if j.isalpha()])
            if len(lst) > len(largest):
                largest = lst
            elif len(lst) == len(largest):
                largest = largest

    print(largest)


largestword("funn&!! time")
