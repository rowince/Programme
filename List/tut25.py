# Python program to count positive and negative numbers in a list

# Input: list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3

list1 = [2, -7, 5, -64, -14]

# for loop

pos = 0
neg = 0
for i in list1:
    if i>0:
        pos+=1
    elif i < 0:
        neg+=1

print(pos)
print(neg)