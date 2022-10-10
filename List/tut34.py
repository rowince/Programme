# Sum of number digits in dictionary in key value pair

# input: x = [12, 67, 98, 34]
# output : {12: 3, 67: 13, 98: 17, 34: 7}

x = [12, 67, 98, 34]
y = {}
for i in x:
    add = 0
    for j in str(i):
        add = add + int(j)
    y[i] = add
print(y)
