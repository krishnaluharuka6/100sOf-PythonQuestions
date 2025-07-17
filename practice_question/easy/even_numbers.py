# print even numbers from 1 to 10

# here i used list comprehension
even_numbers = [i for i in range(1,11) if i%2==0]
print(even_numbers)



# this can also be solved using traditional loop method as
for i in range(1,11):
    if i%2==0:
        print(i, end=" ")