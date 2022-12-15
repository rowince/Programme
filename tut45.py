# Python – Extract words starting with K in String List
# Input : test_list = [“Gfg is good for learning”, “Gfg is for geeks”, “I love G4G”]
# K = l 
# Output : [‘learning’, ‘love’] 
# Explanation : All elements with L as starting letter are extracted.

list1 = ['Gfg is good for learning', 'Gfg is for geeks', 'I love G4G']
# for loop
# list2 = []
# for i in list1:
#     for j in i.split():
#         if j[0].lower() == 'l':
#             list2.append(j)
# print(list2)

# list comprehension

# list2 = [[i for i in x.split() if i[0].lower=='l'] for x in list1]
list2 = [i for x in list1 for i in x.split() if i[0].lower() == 'l' ]
print(list2)