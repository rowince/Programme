# phone number validation
# len should be 10
# all the numebrs are digit
# first number shod be start [6, 7, 8]
from string import digits

x = 99999999999
def phone_valid(val):
    valid = [7, 8, 9]
    y = list(str(val))
    flag = False
    z = int(y[0])
    if len(y) == 10 and z in valid:
        for i in y:
            # i = int(i)
            if i in digits:
                flag = True
    if flag:
        print('valid')
    else:
        print('Invalid')

phone_valid(x)