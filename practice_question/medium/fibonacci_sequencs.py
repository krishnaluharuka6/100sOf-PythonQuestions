# print fibonacci sequence up to 10 term

# 1 1 2 3 5 8 13 21 34

a = 1
b = 1
for i in range(1,10):
    c=a+b
    print(a, end=" ")
    a,b=b,c
