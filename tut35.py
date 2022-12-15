# multiply of number digits in dictionary in key value pair

# input: x = [12, 67, 98, 34]
# output: y = {12: 2, 67: 42, 98: 72, 34: 12}

x = [12, 67, 98, 34]
y = {}
for i in x:
    mul = 1
    for j in str(i):
        mul = mul * int(j)
    y[i] = mul
print(y)