# python programme to sort the even and odd number in list

# Input: list2 = [12, 14, 95, 3, 73]
# Output: [12, 14, 3, 73, 95]

list2 = [12, 14, 95, 3, 73]

def evenodd(list2):
    new = []
    odd_new = []
    for i in list2:
        if i % 2 == 0:
            new.append(i)
            new.sort()
        else:
            odd_new.append(i)
            odd_new.sort()
    new.extend(odd_new)
    print(new)

evenodd(list2)
        
    