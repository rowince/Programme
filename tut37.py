# Python Program to check Armstrong Number

# Input : 153
# Output : Yes
# 153 is an Armstrong number.
# 1*1*1 + 5*5*5 + 3*3*3 = 153

x = 153
sum = 0
temp = x

while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** 3)
    temp = temp // 10

if x == sum:
    print(x, "is armstrong number")
else:
    print(x, "is not armstrong number")


def armstrong_no(x):
    arm = 0
    for i in str(x):
        mul = int(i)*int(i)*int(i)
        arm = arm + mul
    if arm == x:
        print('Yes')
    else:
        print('No')


armstrong_no(x)
