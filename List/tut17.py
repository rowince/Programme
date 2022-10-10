# # Python program to find second smallest number in a list

# Input: list2 = [70, 11, 20, 4, 100]
# Output: 70

# list2 = [70, 11, 20, 4, 100]
list2 = [10, 10, 10, 4, 50]
secmn = max(list2[0], list2[1])
mn = min(list2[0], list2[1])

for i in range(2, len(list2)):
    if list2[i] < secmn and list2[i] > mn:
        secmn = list2[i]
    elif list2[i] < mn:
        secmn = mn
        mn = list2[i]

print(secmn)
