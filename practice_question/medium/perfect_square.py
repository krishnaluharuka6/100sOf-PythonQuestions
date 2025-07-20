num = int(input("Enter a number"))
i = 1
is_perfect_square = False
while i <= num ** 0.5:
    if(i*i == num):
        is_perfect_square = True
        break
    i += 1

if(is_perfect_square):
    print(f"{num} is perfect square")
else:
    print(f"{num} is not perfect square")
