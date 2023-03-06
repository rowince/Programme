# concept

# def extendList(val, list=[]):
#     list.append(val)
#     return list


# list1 = extendList(10)
# list2 = extendList(123, [])
# list3 = extendList('a')

# print(list1) # [10]
# # print(id(list1))
# print(list2) # [123]
# # print(id(list2))
# print(list3) # [10, 'a']
# # print(id(list3))

##################################################################

# def multipliers(x):
#     y = [lambda x: i * x for i in range(4)]
#     print(y)

# multipliers(2)
# for i in multipliers():
#     print(i(2))
# print([m(2) for m in multipliers()])

# list = [ [ ] ] * 5
# print(list)  # output? [[], [], [], [], []]
# print(id(list))
# list[0].append(10)
# print(list)  # output? [[10], [], [], [], []]
# print(id(list))
# list[1].append(20)
# print(list)  # output? [[10], [20], [], [], []]
# print(id(list))
# list.append(30)
# print(list)  # output? [[10], [20], [], [], [], 30]
# print(id(list))


# print(x)
# print(id(x))
# print(id(x[0]))
# print(id(x[1]))
# print(id(x[2]))
# print(id(x[3]))
# print(id(x[4]))
# print(y)
# print(id(y))
# print(id(y[0]))
# print(id(y[1]))
# print(id(y[2]))
# print(id(y[3]))
# print(id(y[4]))
# print(x)
# print(id(x))
# x[0].append(10)
# print(id(x[0].append(10)))
# print(x)
# print(y)
# print(id(y))
# y[0].append(10)
# print(y)
# print(x)
# x[0].append(10)
# print(x)

###############################################################
# x = [{}]*5
# y = [[], [], [], [], []]

# print(x)
# z = set()
# print(type(z))
# z.add(10)
# print(z)
