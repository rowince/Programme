import time

# Python | Ways to find length of list

x = [ 1, 4, 5, 7, 8 ]

#built-in method
# start = time.time()
# size = len(x)
# print("Lenagth:", size)
# end = time.time()
# print("Time_Taken:", end-start)

# using for loop
start = time.time()
size = 0
for i in x:
    size = size + 1
print("Length:", size)
end = time.time()
print("Time_Taken:", end-start)


