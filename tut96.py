# parenthesis balancing program in python
# Input = {[]{()}}
# Output = Balanced

# Input = [{}{}(]
# Output = Unbalanced

# x = '{[]{()}}'
# x = '[{}{}(]'
x = '[[[[[({{}]]]]]'

def parenthesis_balanced(val):
    open = ["[", "{", "("]
    close = ["]", "}", ")"]
    lst = []
    flag = True
    for i in val:
        if i in open:
            lst.append(i)
        else:
            pos = close.index(i)
            if (len(lst)>0) and (open[pos] == lst[len(lst)-1]):
                lst.pop()
            else:
                return "UnBalanced"
    if len(lst) == 0:
        return "Balanced"
    else:
        return "UnBalanced"

print(parenthesis_balanced(x))

    

