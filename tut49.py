# python program to find the larget word in the strings

def largestword(str):
    word = str.split()
    largest = ''
    for i in word:
        if i.isalpha() or i.isnumeric():
            if len(i) > len(largest):
                largest = i
            elif len(i) == len(largest):
                largest = largest
    print(largest)


largestword("fun&!! time")