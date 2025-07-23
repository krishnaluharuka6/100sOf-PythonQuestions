""" You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself."""

x = [0]
y = [0]

x_len = len(x)
y_len = len(y)

if x_len != y_len:
    min = min(x_len, y_len)
    max = max(x_len, y_len)
    for i in range(min, max):
        if x_len < y_len:
            x.append(0)
        else:
            y.append(0)

x = x[::-1]
y = y[::-1]
print(x,y)
c = 0
output = ""



for i in range(-1, -(len(x)+1),-1):
    sum = x[i] + y[i] + c
    if sum < 10:
        output = str(sum) + output
        c = 0
    else:
        sum = str(sum)
        output = sum[-1] + output
        c = 1

if c==1:
    output = "1" + output


