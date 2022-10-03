import copy
import time

# find consecutive numbers in an array in python
# input = [1, 2, 3, 8, 5, 6, 9, 3, 4]
# output = [ [1, 2, 3], [5, 6], [3, 4] ]

input = [1, 2, 3, 8, 5, 6, 9, 3, 4]


def consecutive(input):
    size = len(input)
    output = []
    for k in range(1):
        out = []
        i = k
        for j in range(1, size):
            if input[j] == input[i]+1:
                if input[i] not in out:
                    out.append(input[i])
                if input[j] not in out:
                    out.append(input[j])
            else:
                if len(out) != 0:
                    output.append(copy.deepcopy(out))
                    out.clear()
            i += 1
        else:
            if len(out) != 0:
                output.append(copy.deepcopy(out))
                out.clear()
    print(output)
start = time.time()
consecutive(input)
end = time.time()
print('Time Taken:', end-start)
