# print squares of numbers from 1 to 5

# here i used list comprehension
squares = [i ** 2 for i in range(1,6)]
print(squares)


# Using traditional method

for i in range(1,6):
    print(i ** 2, end=" ")