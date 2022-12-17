x = 'aaaBBbBdCCEFfe'
# output = 'aABbdCcEFfe


# def str_check(x):
#     new = ''
#     for i in x:
#         if i.islower() and i not in new:
#             new = new + i
#         elif i.islower():
#             new_i = i.upper()
#             if new_i not in new:
#                 new = new + new_i
#         else:
#             if i.isupper() and i not in new:
#                 new = new + i
#             elif i.isupper():
#                 li = i.lower()
#                 if li not in new:
#                     new = new + li

#     print(new)
# str_check(x)

def str_check(x):
    new = ''
    for i in x:
        if i.islower():
            if i not in new:
                new = new + i
            else:
                if i.upper() not in new:
                    new = new + i.upper()
        else:
            if i.isupper():
                if i not in new:
                    new = new + i
                else:
                    if i.lower() not in new:
                        new = new + i.lower()
    print(new)


str_check(x)
