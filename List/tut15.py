# Python program to find largest number in a list

# Input : list2 = [20, 10, 20, 4, 100]
# Output : 100

list2 = [20, 10, 20, 4, 100]

# max function

# x = max(list2)
# print(x)

# sort function

# list2.sort()
# print(list2[-1])

# for loop

mx = list2[0]
for i in range(len(list2)):
    if list2[i] > mx:
        mx = list2[i]
print(mx)